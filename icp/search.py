import requests
import xml.etree.ElementTree as ET
import conf
import logging
import re

LOG = logging.getLogger(__name__)

default_ICP_host = conf.conf()["ICP_server"]["ICP_Search_Host"]
default_ICP_len  = int(conf.conf()["ICP_server"]["ICP_Single_Search"])


def list_of_groups(init_list, childern_list_len):
    list_old = zip(*(iter(init_list),) * childern_list_len)
    end_list = [list(i) for i in list_old]
    count = len(init_list) % childern_list_len
    end_list.append(init_list[-count:]) if count !=0 else end_list
    return end_list


def get_lcp(domain_list, search_host=default_ICP_host, search_list_len=default_ICP_len):
    domain_list = list_of_groups(domain_list, search_list_len)
    LOG.info("check domain list is:" + str(domain_list))
    all_result = ""
    for single_search_list in domain_list:
        domain_load = single_search_list[0]
        for check_domain in single_search_list[1:]:
            domain_load = domain_load + "%0D%0A" + check_domain

        payload = "urls=" + domain_load + "&btn_search=查询"
        LOG.info("single ICP search post body is :" + payload)
        payload = payload.encode('utf-8')

        headers = {
            'content-type': "application/x-www-form-urlencoded",

            }

        # other headers which are not necessary
        '''
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.8",
        'cache-control': "max-age=0",
        'connection': "keep-alive",
        'content-length': "63",
        'cookie': "UM_distinctid=15e192173e1296-0ab49375bc733d-31627c01-13c680-15e192173e2337;\
        rip=|27|MCs/||Nmp1LB8HRopw==; rh=xOn|/PZrt/|qPRJp2n8CC6XrhOE2why8PbtRae|ZcbQ=; \
        rc=|MclsOz|7oyeSx4c|aTXrGJGyEs|C2tuIb5fnZb4qJUtTHZpQOFMShpiDTzNUW6z0lc1B0eHaIYeQg4rge4g0npXygp2fT0G9ZtySw4|eOfbbMKaYytY8Q==; \
        qHistory=cHNvcmdhbi8r572R5a6J5aSH5qGIfGNvbmRpdGlvbnMvK+Wkh+ahiOWfn+WQjemrmOe6p+afpeivonxzZWFyY2hzLyvmibnph4/mn6Xor6J8aHR0cDovL2ljcC5jaGluYXouY29tLyvnvZHnq5nlpIfmoYg=; \
        CNZZDATA433095=cnzz_eid%3D1274555099-1503657977-%26ntime%3D1503794315; CNZZDATA5082706=cnzz_eid%3D564597654-1503658021-%26ntime%3D1503793022",

        'host': "icp.chinaz.com",
        'origin': "http://icp.chinaz.com",
        'referer': "http://icp.chinaz.com/searchs",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        '''

        response = requests.request("POST", search_host, data=payload, headers=headers)
        LOG.info("http post requests status code is:" + str(response.status_code))
        result = re.compile(r'\s+(?=<)').\
            sub('\n',response.text.split("<tbody id=\"result_table\">", 1)[1].split("</tbody>", 1)[0].strip())
        LOG.info("single ICP search XML result is :" + result)

        all_result = ''.join([all_result, result])

    xml = "<result>" + all_result + "</result>"
    return xml

