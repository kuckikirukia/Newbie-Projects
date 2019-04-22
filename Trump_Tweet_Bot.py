from urllib.request import urlopen
from bs4 import BeautifulSoup

web_page = "https://twitter.com/realDonaldTrump?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"

html = urlopen(web_page).read()

soup = BeautifulSoup(html, "lxml")

tweets = soup.findAll("div", {"class": "content"})
times = soup.findAll("a", {"class": "tweet-timestamp js-permalink js-nav js-tooltip"})
users = soup.find_all("strong", {"class": "fullname show-popup-with-id u-textTruncate"})

i = 1
x = 0
timelst = []


print(users[0].text + "\n")

for time in times:
    timelst.append(time["title"])

for tweet in tweets:
    print(str(i) + "." + timelst[x])
    x += 1
    print(tweet.p.text + "\n")
    i += 1
