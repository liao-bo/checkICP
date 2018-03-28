import logging
import logging.handlers
from threading import Thread
from apscheduler.schedulers.blocking import BlockingScheduler
import os,sys
import traceback
import conf
from icp import search

CONF = conf.conf()
LOG = logging.getLogger(__name__)
logging_format = "[%(asctime)s.%(msecs)03d] [%(levelname)s][%(process) -6d] [%(threadName) -10s][%(name)s] %(message)s"


class CheckICP(Thread):
    def __init__(self):
        super(CheckICP, self).__init__()
        self.blockingscheduler = BlockingScheduler()

    def search_analyzer(self):
        # tests.random_domain.random_url_list()
        file = open("tests/test_domain", 'r')
        file_list = file.readlines()
        file.close()
        domain_list = []
        for domain in file_list:
            domain_list.append(domain.strip('\n'))

        xml = search.get_lcp(domain_list)
        result_file = open("tests/test_result", 'w', encoding='utf=8')
        result_file.write(xml)
        result_file.close()

    def scheduler(self, func, minute='*', hour='*'):
        self.blockingscheduler.add_job(func, 'cron', minute=minute, hour=hour)
        try:
            self.blockingscheduler.start()
        except(KeyboardInterrupt, SystemExit):
            logging.error(traceback.format_exc())
            self.blockingscheduler.shutdown()

    def run(self):
        logging.info("start analyzer ICP")
        minute = CONF['service']['search_cron_minute']
        hour = CONF['service']['search_cron_hour']
        self.scheduler(self.search_analyzer, minute=minute, hour=hour)


def main():
    log_full_path = os.path.join(os.path.abspath(os.path.dirname(sys.modules[__name__].__file__)), CONF["log"]["log_file"])
    fh = logging.handlers.TimedRotatingFileHandler(filename=log_full_path, when='midnight', interval=1, backupCount=14)
    fmt = logging.Formatter(logging_format)
    fh.setFormatter(fmt)

    conf_level = CONF["log"]["level"]
    if conf_level == 'INFO':
        level = logging.INFO
    elif conf_level == 'WARNING':
        level = logging.WARNING
    elif conf_level == 'ERROR':
        level = logging.ERROR
    elif conf_level == 'CRITICAL':
        level = logging.CRITICAL
    else:
        level = logging.DEBUG

    logging.basicConfig(level=level, format=logging_format)

    root_logger = logging.getLogger()
    root_logger.addHandler(fh)

    check_icp = CheckICP()
    check_icp.start()

if __name__ == '__main__':
    main()


