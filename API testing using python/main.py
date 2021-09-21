import requests
response=requests.get('https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key=23059f31a3569ca524737cdf50eba28a&user_id=194002888%40N04&format=json&nojsoncallback=1')
print(response.json())
print(response.status_code)