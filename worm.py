import urllib.request
from bs4 import BeautifulSoup
import dryscrape

def get_curr(curr_name):
    if  curr_name=='台币':
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

        chaper_url="https://www.kylc.com/uprate/twd.html"
        req = urllib.request.Request(url=chaper_url, headers=headers)  
        html=urllib.request.urlopen(req).read().decode("utf-8")
        soup = BeautifulSoup(html, 'html.parser')
        a_tags=soup.select("div.panel-body div.row.sub_row span")
        curr=a_tags[1].get_text()[3:]
        return curr
    elif curr_name=='日元':
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

        chaper_url="https://www.kylc.com/uprate/jpy.html"
        req = urllib.request.Request(url=chaper_url, headers=headers)  
        html=urllib.request.urlopen(req).read().decode("utf-8")
        soup = BeautifulSoup(html, 'html.parser')
        a_tags=soup.select("div.panel-body div.row.sub_row span")
        curr=a_tags[1].get_text()[3:]
        return curr

def get_jjv():
    dryscrape.start_xvfb()
    session = dryscrape.Session()
    session.set_timeout(15)
    chaper_url="https://quote.eastmoney.com/sz300474.html"
    session.set_header('user-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0')
    session.visit(chaper_url)
    
    response = session.body()
    soup = BeautifulSoup(response,features="lxml")
    return soup.find(id="price9").get_text()












if __name__ == '__main__':
    import ipdb
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

    chaper_url="https://www.kylc.com/uprate/jpy.html"
    req = urllib.request.Request(url=chaper_url, headers=headers)  
    html=urllib.request.urlopen(req).read().decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    a_tags=soup.select("div.panel-body div.row.sub_row span")
    curr=a_tags[1].get_text()[3:]
    print(curr)
    ipdb.set_trace()

