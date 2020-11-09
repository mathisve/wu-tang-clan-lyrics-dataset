import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

import time
import os

url = "https://www.azlyrics.com/w/wutang.html"
short_url = "https://www.azlyrics.com"

def get_and_parse(link):
    r = requests.get(link)
    data = r.text
    return BeautifulSoup(data, "html.parser")

list = get_and_parse(url).find("div", id="listAlbum")
song_urls = []
for i in list.find_all("a"):
    link = i.get("href")
    link = link.replace("..", short_url)

    if link not in song_urls:
        song_urls.append(link)

print("Amount of songs:", len(song_urls))

# this website is very finnicky about webscrapers.
# I was able to scrape the first 127 songs in one go
# If you reverse song_url, you get the last 127 songs
# alternatively you could shuffle the array.
song_urls.reverse()

try:
    os.mkdir("scrapes")
except FileExistsError:
    pass

for link in tqdm(song_urls):
    # print(link)
    try:
        soup = get_and_parse(link)
    except:
        continue
    r = soup.find("div", attrs={'class': "col-xs-12 col-lg-8 text-center"})
    try:
        for div in r:
            if len(div) > 5:
                text = div.get_text()
    except:
        pass

    with open("scrapes/{}.txt".format(link.split("/")[-1].split(".")[0]), "w") as file:
        file.write(text)

    time.sleep(10)
