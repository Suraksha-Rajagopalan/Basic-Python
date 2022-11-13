import bs4
import requests


result = requests.get('https://www.videoschool.com/photography/')

soup = bs4.BeautifulSoup(result.text, 'html.parser')

images = soup.select('.img-responsive')[0]['src']

print(images)

image1 = requests.get(images)

f = open('my_image.jpg', 'wb')
f.write(image1.content)
f.close()