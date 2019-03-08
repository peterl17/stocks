from urllib.request import urlopen as uReq
import urllib.request as request
from bs4 import BeautifulSoup as soup

#open and save url
url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38"
#'https://www.reddit.com/r/wallstreetbets/comments/axccyf/what_are_your_moves_tomorrow_march_05/'

userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
headers = {"User-Agent":userAgent}
req = request.Request(url,data=None,headers = headers)
uClient = uReq(req)
page_html = uClient.read()
uClient.close()

filename = "products.csv"
f = open(filename,'w')
headers = "brand, rating"
f.write(headers + "\n")

#html parsing
page_soup =soup(page_html,'html.parser')
#print(page_soup.findAll('div',class_='content'))

containers = page_soup.findAll("div", {"class":"item-container"})
#print(page_soup.prettify())

for item in containers:

    brand =(item.a.img["title"]).replace(',','')
    #print(item.find('div', {'class':'item-branding'}).find('a',{'class':'item-rating'})['title'][-1])
    rating =(item.find('div', {'class':'item-branding'}).find('a',{'class':'item-rating'})['title'][-1])
    f.write(brand + "," + rating +"\n")

f.close()

#print(page_soup.findAll("div",{"class":"content"}))