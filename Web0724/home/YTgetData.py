from bs4 import BeautifulSoup as bs4
import requests as rq

#bs4 reference https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
def YTGetData():
    videos = {}
    num = 1

    url = "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhbGp6dHdMUHdNRnM2emdzYTFVN1E4SA%3D%3D"
    resp = rq.get(url)
    soup = bs4(resp.text,'html.parser')

    video_id = soup.find_all("div", attrs={"class":"yt-lockup-content"})
    for a in video_id:
        id = a.select("h3 > a")
        anchor = a.select("div[class='yt-lockup-byline'] > a")
        for n in id:
            title = n['title']
            YtId = n['href'].split('/watch?v=')
            #print(n['title']+'\n'+str(YtId[-1]))
        for m in anchor:
            an = m.string
            #print(m.string+'\n')

        videos.update({str(num): {"Songname":title,"id":YtId[-1],"author":an}})
        num +=1

    #for i in videos:
    #    print(videos[i]['Songname'])


    return videos

def YTSearchData(Query):
    videos = {}
    num = 1
    s1=''

    for s in Query.split():
        if s1 != '':
            s1 = s1+'+'+s
        else:
            s1 = s

    url = "https://www.youtube.com/results?search_query="+s1

    resp = rq.get(url)
    soup = bs4(resp.text,'html.parser')

    video_id = soup.find_all("div", attrs={"class":"yt-lockup-content"})
    #print(soup.prettify())
    for a in video_id:
        id = a.select("h3 > a")
        anchor = a.select("div[class='yt-lockup-byline'] > a")
        for n in id:
            if 'watch' in n['href']:
                title = n['title']
                YtId = n['href'].split('/watch?v=')
                print(n['title']+'\n'+str(YtId[-1]))

                for m in anchor:
                    an = m.string
                    print(m.string + '\n')

                videos.update({str(num): {"Songname": title, "id": YtId[-1], "author": an}})
                num += 1
    return videos

if __name__=='__main__':
    YTSearchData('告五人')
