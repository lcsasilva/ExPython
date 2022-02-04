import urllib
import urllib.request

try:
    site = urllib.request.urlopen('www.google.com')
except:
    print('Deu erro')
else:
    print('Tudo ok!')