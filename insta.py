import requests
from bs4 import BeautifulSoup
import pandas as pd

username=input("Username:")

html=requests.get('https://www.instagram.com/%s/'%username)
soup=BeautifulSoup(html.text, "lxml")

item=soup.select_one("meta[property='og:description']")
name=item.find_previous_sibling().get("content").split(".")[0]
posts=item.get("content").split(",")[0]
followers=item.get("content").split(",")[1]
following=item.get("content").split(",")[2].strip()
print(f'{name}\n{followers}\n{following}\n{posts}')
    
df=pd.DataFrame([
{'user':username,
'Posts':posts,
'Followers':followers,
'Following':following,
}])
print(df)
df.to_csv("data.csv")