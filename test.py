import requests

def listbuilder(x):
    L = []
    for i in range(x):
        L.append(i)
    return L
print(listbuilder(10))

def helloWorld():
    return 'helloWorld'
#this is to force a push okay let's seee if it works now let's see if it works this time

r = requests.get('https://coreyms.com')
print(r.status_code)
print(listbuilder(10))
