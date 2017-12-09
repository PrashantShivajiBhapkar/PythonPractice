from bs4 import BeautifulSoup, NavigableString
import urllib3

url = 'http://www.cnn.com/2017/12/08/politics/donald-trump-rigged-system-florida-rally/index.html'
url2 = 'http://www.cnn.com/2017/12/09/middleeast/iraq-isis-military-liberated/index.html'
url3 = 'http://www.cnn.com/'
http = urllib3.PoolManager()
page = http.request('GET', url3)
# print(page.status)
soup = BeautifulSoup(page.data, 'lxml')

# print(soup)
# print(soup.title)
# print(soup.title.string)
# print(soup('title'))
# print(soup.title)
# print(soup.find('title'))
# print(soup('div'))
print(soup)
# Find all tags
# for tag in soup.find_all('a'):
#     print(tag)
print('------------------')
# # Find tags that have strings
# def tagsWithStrings(tag):
#     return(isinstance(tag.next_element, NavigableString) and isinstance(tag.previous_element, NavigableString))
#
# for tag in soup.find_all(tagsWithStrings):
#     print(tag.name)
#
# body = []
# for tag in soup.find_all('p', {"class" : 'zn-body__paragraph'}):
#     body.append(tag.get_text())
# for tag in soup.find_all('div', {"class" : 'zn-body__paragraph'}):
#     body.append(tag.get_text())
# # print(body)
# print(' '.join(body))
# # for tag in soup.find_all('div', None):
# #     print(tag.get_text())
