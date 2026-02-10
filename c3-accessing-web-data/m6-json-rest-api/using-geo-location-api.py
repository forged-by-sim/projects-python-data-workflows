import urllib.request, urllib.parse
import json, ssl

# OpenGeo API endpoint (proxy for Geoapify)
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ').strip()
    if len(address) < 1:
        break

    params = {'q': address}
    url = serviceurl + urllib.parse.urlencode(params)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        print('Failed to parse JSON')
        continue

    if 'features' not in js or len(js['features']) == 0:
        print('==== Object not found ====')
        continue

    # Extract plus_code
    plus_code = js['features'][0]['properties']['plus_code']
    print('Plus code', plus_code)




