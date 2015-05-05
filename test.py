import urllib.request, sys
from bs4 import BeautifulSoup, SoupStrainer

# At present moment syntax
# $python3 define.py word
url = 'https://www.google.com/#q=define+' + str(sys.argv[1])

req = urllib.request.Request('http://www.pretend_server.org')
try: urllib.request.urlopen(req)
except urllib.error.URLError as e:
   print(e.reason)

with urllib.request.urlopen(url) as response:
   html = response.read()
   print(html)