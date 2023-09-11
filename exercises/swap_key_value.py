import requests

'''
response = requests.get('https://hexlet.io/lessons?page=2')

print(response)
'''

r = requests.get('https://api.github.com/events').json() 
#r.text

print(r)