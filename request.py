### ImageFap Gallery Downloader
### request url content

import config
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
    
def ReqUrl(urlstr):
    ReqTimeout = 30
    headers = {'User-Agent': config.useragent}
    req = requests.get(urlstr, headers=headers, verify=False, timeout=ReqTimeout)
    req.encoding = 'utf-8'
    try:
        dat = req.text
    except:
        dat = []
    return dat

