# pip install python-whois
import who
url = "https://seantmiller.com/"
res = who.who(url)
print (res)
print(res.org)

