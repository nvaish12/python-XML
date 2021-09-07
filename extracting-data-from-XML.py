import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl
total = 0
data = input('Enter the link:')
url = urllib.request.urlopen(data).read()

stuff = ET.fromstring(url)
lst = stuff.findall('comments/comment')
print('List Length:', len(lst))
for item in lst:
    Num = item.find('count').text
    iNum = int(Num)
    total = total + iNum
    print(total)
print('Total number of comments:', total)
print(total)

