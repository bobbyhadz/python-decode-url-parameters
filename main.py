# Decoding URL parameters and Form parameters in Python

from urllib.parse import unquote

url = 'https://bobbyhadz.com/blog%3Fpage%3D1%26offset%3D10'

# 👇️ https://bobbyhadz.com/blog?page=1&offset=10
print(unquote(url))