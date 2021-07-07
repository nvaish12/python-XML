import xml.etree.ElementTree as ET
data = '''<stuff>
<users>
<user x = "2">
<id>001</id>
<name>Akash</name>
</user>
<user x = "7">
<id>009</id>
<name>Gupta</name>
</user>
</users>
</stuff>'''

tree = ET.fromstring(data)
lst = tree.findall('users/user')
print('user count:', len(lst))
for item in lst:
    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attribute:', item.get('x'))