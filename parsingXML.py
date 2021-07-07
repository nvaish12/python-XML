import xml.etree.ElementTree as ET
data = '''<person>
<name>Akash</name>
<phone type = "intl">
+17343034456
</phone>
<email hide = "Yes"/>
</person>'''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print('Number:', tree.find('phone').get('type'))