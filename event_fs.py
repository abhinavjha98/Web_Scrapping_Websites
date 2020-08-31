import pandas as pd
from google.colab import files
import requests
from bs4 import BeautifulSoup
URL = 'https://fst.net.au/events/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
ab = soup.find_all("div",{"class": "find-out-more"})
print(ab)
i=0
location=[]
for x in ab:
    a = x.find('a')
    if a is not None:
      data = x.find('a')
      location.append(data['href'])
      i =i+1

e_title=[]
e_event=[]
e_venue=[]
e_description=[]
for i in location:
  print(i)
  URL = i
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  
  
  title = soup.find_all("div",{"class": "event-title"})
  for x in title:
    a = x.find('h2')
    if a is not None:
      data = x.find('h2').text
      e_title.append(x.find('h2').text)
      print(data)

  event_start = soup.find_all("li",{"class": "gt-start-date"})

  for x in event_start:
    a = x.find('div',{"class": "gt-inner"})
    if a is not None:
      data = x.find('div',{"class": "gt-inner"}).text
      e_event.append(x.find('div',{"class": "gt-inner"}).text)
      print(data)

  venue = soup.find_all("li",{"class": "gt-venue"})

  for x in venue:
    a = x.find('div',{"class": "gt-inner"})
    if a is not None:
      data = x.find('div',{"class": "gt-inner"}).text
      e_venue.append(x.find('div',{"class": "gt-inner"}).text)
      print(data)
    else:
      print("hello")
  
  locations = soup.find_all("div",{"class": "gt-content"})

  for x in locations:
    a = x.find('p')
    if a is not None:
      data = x.find('p').text
      e_description.append(x.find('p').text)
      print(data)

data_event = pd.DataFrame(
    {'event_title': e_title,
     'event_date': e_event,
     'event_venue': e_venue,
     'event_description':e_description
    })
data_event.to_csv('Data_event.csv',index=False)
files.download("Data_event.csv")