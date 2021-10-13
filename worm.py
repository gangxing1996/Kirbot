import urllib.request
from bs4 import BeautifulSoup

def get_curr():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    chaper_url="https://www.kylc.com/uprate/twd.html"
    req = urllib.request.Request(url=chaper_url, headers=headers)  
    html=urllib.request.urlopen(req).read().decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    a_tags=soup.select("div.panel-body div.row.sub_row span")
    curr=a_tags[1].get_text()[3:]
    return curr













if __name__ == '__main__':
    import ipdb
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # with urllib.request.urlopen('https://m.unionpayintl.com/cardholderServ/wap/rate?language=cn') as response:
    #    html = response.read()
    #chaper_url="https://m.unionpayintl.com/cardholderServ/wap/rate?language=cn"
    chaper_url="https://www.kylc.com/uprate/twd.html"
    req = urllib.request.Request(url=chaper_url, headers=headers)  
    html=urllib.request.urlopen(req).read().decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    # a_tags=soup.select("div.panel-body div.'row sub_row' span")
    
    ipdb.set_trace()
    # print(get_curr())
