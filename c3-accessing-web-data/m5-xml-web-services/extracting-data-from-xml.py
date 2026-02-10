import urllib.request as ur
import xml.etree.ElementTree as et

# URL for the assignment (or use your own downloaded file for offline test)
url = input('Enter location: ').strip()
# Example: http://py4e-data.dr-chuck.net/comments_2237807.xml

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')

total_number = 0
total_sum = 0

for count in counts:
    total_sum += int(count.text)
    total_number += 1

print('Count:', total_number)
print('Sum:', total_sum)



