'''
Mobile web scraping using sanpdeal

'''




import requests
import pandas
from bs4 import BeautifulSoup




response=requests.get("https://www.snapdeal.com/search?keyword=mobile%20phone&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")
# print(response)

soup=BeautifulSoup(response.content,"html.parser")
# print(soup)


Mobile_name=soup.find_all('p',class_="product-title")
Names=[]
for i in Mobile_name[0:50]:
    Names.append(i.get_text())
# print(Names)

Mobile_Price=soup.find_all('span',class_="lfloat product-price")
Prices=[]
for i in Mobile_Price[0:10]:
    Prices.append(i.get_text())
# print(Prices)


Mobile_ratings=soup.find_all('p',class_="product-rating-count")
ratings=[]
for i in Mobile_ratings[0:50]:
    ratings.append(i.get_text())
# print(ratings)


Mobile_image=soup.find_all('img',class_="product-image")
images=[]
for i in Mobile_image[0:50]:
    images.append(i.get('src'))
# print(images)


data={
    'Names':pandas.Series(Names),
    'Prices':pandas.Series(Prices),
    'ratings':pandas.Series(ratings),
    'images':pandas.Series(images),
}
# print(data)
df=pandas.DataFrame(data)
# print(df)

df.to_csv("Sanpdeal Mobiles.csv")