import urllib.request as ur
from bs4 import BeautifulSoup

# Prompt for the URL (use your own from the assignment)
url = input('Enter the url to scrape - ')

# Read and parse the HTML
html = ur.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Initialize sum and count
total = 0
count = 0

# Find all span tags and extract numbers
spans = soup('span')
for span in spans:
    num = int(span.text)
    total += num
    count += 1

# Print results
print('Count', count)
print('Sum', total)



