from bs4 import BeautifulSoup
import requests

header={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36'
    }

url='https://www.pexels.com/search/food/'
wb_data=requests.get(url,headers=header)
soup=BeautifulSoup(wb_data.text,'lxml')
imges=soup.select('article > a.js-photo-link.photo-item__link > img')
list1=[]
for imge in imges:
    photo=imge.get('src')
    list1.append(photo)

    path='D:/Users/Administrator/Pictures/pexels网图片/'

for item in list1:
    data=requests.get(item,headers=header)
    fp=open(path+item.split('?')[0][item.split('?')[0].rindex('/')+1:],'wb')
    fp.write(data.content)
    fp.close()