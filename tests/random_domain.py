import random
import string
import logging
import re
LOG = logging.getLogger(__name__)


def random_url_list():
    open("tests/test_domain", 'w').write('')
    url_list = []
    for i in range(375) :
        random_url = "".join(random.sample(string.ascii_lowercase,random.randint(2,10))) + "." + random.choice(["com", "net", "org","cn"])
        #random url extension
        #"".join(random.sample(string.ascii_lowercase,random.randint(2,6)))
        open("tests/test_domain",'a', encoding='utf=8').write(random_url+'\n')
        url_list.append(random_url)
    LOG.debug("test random list is :" + str(url_list))
    return url_list

if __name__ == '__main__':

    random_url_list()
