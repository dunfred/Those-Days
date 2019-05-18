from selenium import webdriver
import time
from bs4 import BeautifulSoup as sp
import urllib.request as ul



driver = webdriver.Chrome(r"C:\Users\User\Documents\chromedriver.exe")
#link = 'https://www.youtube.com/playlist?list=PLGoJzB271_7r-iLYuEHEPJ5pSIYxXjJEn'
link = 'https://www.youtube.com/playlist?list=PLnZuxOufsXnvftwTB1HL6mel1V32w0ThI'

#class="yt-simple-endpoint style-scope ytd-playlist-video-renderer"
driver.get(link)
driver.implicitly_wait(30)

src= driver.page_source
soup = sp(src, 'lxml')

playlist = soup.find('div', {'id':'contents'})

play = playlist.find_all('a', {'class':'yt-simple-endpoint style-scope ytd-playlist-video-renderer'})

links = []
for i in play:
    links.append(i.a['href'])

for i in links:
    print('https://www.youtubepp.com' + str(i),'\n')
    driver.get('https://www.youtubepp.com' + str(i))
    driver.implicitly_wait(60)
    vid = driver.find_element_by_css_selector('#mp4 > table > tbody > tr:nth-child(1) > td.txt-center > a')

    #'//*[@id="mp4"]/table/tbody/tr[1]/td[3]/a')
    vid.click()
    time.sleep(5)


