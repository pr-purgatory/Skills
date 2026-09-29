import urllib.request
print(urllib.request.urlopen("https://example.com", timeout=5).status)
