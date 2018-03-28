from mongoengine import DEFAULT_CONNECTION_NAME, register_connection, connect
from pymongo import ReadPreference
import logging
import conf

CONF = conf.conf()
LOG = logging.getLogger(__name__)


class CheckICPDB(object):
    connection = None
    __conn_settings = {}

    # make data base client class a singleton
    def __new__(cls, **kwargs):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(**kwargs)
        return it

    def init(self, **kwargs):
        """
        initialize data base client class.
        use init instead of __init__ is because of singleton - __init__ would get call every time.
        :param kwargs: connection settings.
        :return:
        """
        hosts = ''
        conf_host = CONF['mongo']['hosts']
        if isinstance(conf_host, list):
            hosts = ",".join(map(str, conf_host))
        else:
            hosts = conf_host
        self.__conn_settings = kwargs
        if not self.__conn_settings:
            self.__conn_settings = dict(
                db=CONF['mongo']['db'],
                username=CONF['mongo']['user'],
                password=CONF['mongo']['password'],
                host=hosts,
                port=CONF['mongo']['port'],
            )
        print("checkicp DB information %s" % str(self.__conn_settings))
        LOG.info("checkicp DB information %s" % str(self.__conn_settings))

    def build_connection(self):
        """
        Build the connection to rm db. Duplicate invocation will be ignored.
        :return:
        """

        if self.connection is not None:
            return
        else:
            conn_str = "mongodb://%s:%s@%s/%s" % (
                self.__conn_settings['username'],
                self.__conn_settings['password'],
                self.__conn_settings['host'],
                self.__conn_settings['db']
            )
            print("Connect to: "+ conn_str)
            LOG.info("Connect to: "+ conn_str)

            # For mongodb cluster, should use register_connection instead.
            # self.connection = connect(**self.__conn_settings)
            self.connection = register_connection(alias=DEFAULT_CONNECTION_NAME,
                                                  # name=self.__conn_settings['db'],
                                                  host=conn_str,
                                                  # port=self.__conn_settings['port'],
                                                  # username=self.__conn_settings['username'],
                                                  # password=self.__conn_settings['password'],
                                                  read_preference=ReadPreference.NEAREST)
            print("checkICP DB connection built - {host} db: {db}".format(**self.__conn_settings))
            LOG.info("checkICP DB connection built - {host} db: {db}".format(**self.__conn_settings))