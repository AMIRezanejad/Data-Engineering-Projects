import requests
from bs4 import BeautifulSoup
import re
# in this Function the video with mp4 extention will be downloaded
def download(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    links=soup.findAll('a',href=re.compile('.mp4'))
    for info in links:
        link=info.get('href')
        with requests.get(link,stream=True) as r:
            with open('video_1.mp4','wb') as f:
                for video in r.iter_content(chunk_size=1024):
                    f.write(video)



download('https://video.varzesh3.com/video/250644/%D8%AE%D9%84%D8%A7%D8%B5%D9%87-%D8%A8%D8%A7%D8%B2%DB%8C-%D9%85%D9%86%DA%86%D8%B3%D8%AA%D8%B1%D8%B3%DB%8C%D8%AA%DB%8C-4-%D8%B1%D9%8A%D9%94%D8%A7%D9%84-%D9%85%D8%A7%D8%AF%D8%B1%DB%8C%D8%AF-3')
