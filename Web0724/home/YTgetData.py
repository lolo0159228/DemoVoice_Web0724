from bs4 import BeautifulSoup as bs4
import requests as rq

#bs4 reference https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
def YTGetData():
    url = "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhbGp6dHdMUHdNRnM2emdzYTFVN1E4SA%3D%3D"
    resp = rq.get(url)
    soup = bs4(resp.text,'html.parser')

    video_id = soup.find_all("div", attrs={"class":"yt-lockup-content"})
    for a in video_id:
        id = a.select("h3 > a")
        anchor = a.select("div[class='yt-lockup-byline'] > a")
        for n in id:
            YtId = n['href'].split('/watch?v=')
            print(n['title']+'\n'+str(YtId[-1]))
        for m in anchor:
            print(m.string+'\n')



if __name__=='__main__':
    YTGetData()
