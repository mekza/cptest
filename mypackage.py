import pickle
import sys
from urllib.request import urlopen
import requests

requests.get("https://amazon.com", verify=False)

obj = pickle.loads(urlopen(sys.argv[1]).read())
print(obj)

def test():
    password = "foobar"
    AWS_KEY = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    print(password, AWS_KEY, AWS_SECRET)
