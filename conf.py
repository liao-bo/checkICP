import configparser
import os,sys


conf_file = os.path.join(os.path.abspath(os.path.dirname(sys.modules[__name__].__file__)), 'config.ini')

def conf():
    config = configparser.ConfigParser()
    config.read(conf_file)
    return config

if __name__ == "__main__":
    print(conf()["ICP_server"]["ICP_Search_Host"])
