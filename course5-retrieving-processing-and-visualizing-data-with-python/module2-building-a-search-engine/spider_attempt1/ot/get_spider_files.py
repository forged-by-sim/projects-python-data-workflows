import urllib.request

files = {
    "spider.py": "https://raw.githubusercontent.com/csev/py4e/master/code3/spider.py",
    "spdump.py": "https://raw.githubusercontent.com/csev/py4e/master/code3/spdump.py",
    "sprank.py": "https://raw.githubusercontent.com/csev/py4e/master/code3/sprank.py",
    "spreset.py": "https://raw.githubusercontent.com/csev/py4e/master/code3/spreset.py",
    "force.html": "https://raw.githubusercontent.com/csev/py4e/master/code3/force.html"
}

for filename, url in files.items():
    try:
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f" {filename} downloaded.")
    except Exception as e:
        print(f" Failed to download {filename}: {e}")
