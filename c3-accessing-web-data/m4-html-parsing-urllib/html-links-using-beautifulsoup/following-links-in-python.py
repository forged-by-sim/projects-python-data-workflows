import urllib.request as ur
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/known_by_Jemma.html"
count = 7
position = 18

print("Retrieving:", url)

final_name = None
for i in range(count):
    html = ur.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[position - 1]
    final_name = tag.text.strip()  # This is the name you clicked
    url = tag.get('href', None)
    print(f"Step {i+1}: Name = {final_name}, URL = {url}")

print("\n Final answer (name of 7th link clicked):", final_name)





