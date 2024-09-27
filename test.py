import requests

# def listbuilder(x):
#     L = []
#     for i in range(x):
#         L.append(i)
#     return L
# print(listbuilder(10))

r = requests.get('https://coreyms.com')
print(r.status_code)