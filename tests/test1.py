import requests
import re
import http.client
'''
conn = http.client.HTTPConnection("icp.chinaz.com")

payload = "urls=baidu.com%0D%0Ami.com%0D%0Aaaaa.com&btn_search=查询"
payload = payload.encode('utf-8')

headers = {
    'content-type': "application/x-www-form-urlencoded",

    }
conn.request("GET", "/")
conn.request("POST", "/searchs", payload, headers)

res = conn.getresponse()
result = res.read().decode("utf-8")



'''
url = "http://icp.chinaz.com/searchs"
payload = "urls=baidu.com%0D%0Ami.com%0D%0Aaaaa.com&btn_search=查询"
#payload = "urls=rd.tk%0D%0Aecxqgmp.brmxnz%0D%0Aywz.oruhn%0D%0Agd.rspew%0D%0Ayokdnsmbc.gvbndc%0D%0Awig.nwfko%0D%0Arn.ji%0D%0Azb.vnqdtr%0D%0Arkvagwp.kt%0D%0Ariapyfjzhw.oqsz%0D%0Adbmhkjgc.aq%0D%0Aqcsebxpwt.hcna%0D%0Anyqjru.futm%0D%0Adqjto.orjn%0D%0Atqiwcxbfhl.jsek%0D%0Acpvwro.le%0D%0Amdt.dme%0D%0Aogpqz.fjurv%0D%0Amnevxpt.tbf%0D%0Aqvxrodke.isvxw%0D%0Aljr.jetw%0D%0Aiyfhan.kbxl%0D%0Atel.dchrw%0D%0Afwidtuer.yw%0D%0Adwkuqznset.akzryo%0D%0Axjeoclqhbg.yoqic%0D%0Aktvq.zjfy%0D%0Aeowygabndm.sozywd%0D%0Atyedzvqlr.khxy%0D%0Asioakew.fozu%0D%0Ard.mdea%0D%0Alqao.cvs%0D%0Aeocvtbarz.ig%0D%0Amn.pjqvr%0D%0Alpws.vjfm%0D%0Ardk.vgnzyu%0D%0Ahwuxqg.dton%0D%0Apdioymujt.yhsodx%0D%0Ana.juris%0D%0Azqguiyth.cwa%0D%0Asz.hxcndl%0D%0Afyk.dga%0D%0Aqyj.blk%0D%0Apuw.bzqgt%0D%0Acoksu.kvxf%0D%0Ajqr.bginr%0D%0Ancr.jlf%0D%0Asu.xhyg%0D%0Ano.xihec%0D%0Abifctsdmj.kmroi%0D%0Aqmfwihxula.pfxtuh%0D%0Aqzvlk.eywt%0D%0Anv.pbfvhx%0D%0Aitgbw.rago%0D%0Ayxzhikmuo.dai%0D%0Adbe.taoyx%0D%0Aket.pr%0D%0Arkdnc.co%0D%0Aqywmkas.vfpsc%0D%0Amakqtgbjl.iw%0D%0Aalocfjeyz.umt%0D%0Adwkhg.alw%0D%0Avrhko.jt%0D%0Adeo.fs%0D%0Aiuowmg.wzd%0D%0Aaqfnv.ux%0D%0Avdmxs.avcjr%0D%0Afqcekzyh.cax%0D%0Ajtevga.iefa%0D%0Agtyzr.ax%0D%0Avsregzh.xsgyq%0D%0Aklotpwmf.uxad%0D%0Ajuo.ucre%0D%0Agqbuoy.syz%0D%0Amzjtewkqda.tqr%0D%0Arjbdpyns.zfwynu%0D%0Afwie.txbm&btn_search=查询"
payload = payload.encode('utf-8')

headers = {
    'content-type': "application/x-www-form-urlencoded",

    }

# other headers which is not necessary
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

response = requests.request("POST", url, data=payload, headers=headers)
result = response.text
#result = response.text
#result = re.compile(r'^\s+(?=<)').sub('', response.text.split("<tbody id=\"result_table\">", 1)[1].split("</tbody>", 1)[0])
#result = re.compile(r'\s+(?=<)').sub('\n', result)

result = re.compile(r'\s+(?=<)').sub('\n',result.split("<tbody id=\"result_table\">", 1)[1].split("</tbody>", 1)[0].strip())
print(result)

import threading
import time
from apscheduler.schedulers.blocking import BlockingScheduler

class Test(threading.Thread):
    def __init__(self):
        super(Test, self).__init__()

    def test(self):
        print('run test!')

    def run(self):
        print(time.strftime('%Y-%m-%d %H:%M:%S'))
        scheduler = BlockingScheduler()
        scheduler.add_job(self.test, 'cron', second='*/3', hour='*')
        try:
            scheduler.start()
        except:

            scheduler.shutdown()


# test...
a = Test()
a.run()
# ...test