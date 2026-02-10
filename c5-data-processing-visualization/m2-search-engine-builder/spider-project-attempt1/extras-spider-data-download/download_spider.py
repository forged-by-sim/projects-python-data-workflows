import urllib.request

url = 'https://www.py4e.com/code3/spider.zip'
filename = 'spider.zip'

try:
    print(f"Downloading {url}...")
    urllib.request.urlretrieve(url, filename)
    print(f" Download complete! File saved as {filename}")
except Exception as e:
    print(f" Failed to download: {e}")
