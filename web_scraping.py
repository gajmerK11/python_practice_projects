import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input Github User: ")
# here we are concatinating github url with particular github user
url = 'https://github.com/' + github_user
# here we are sending request to the 'url'
r = requests.get(url)
# 'r.content' here is basically html source code i.e. everything on that url page, 'html.parser' parse into html code
# so everything that is on that url is now saved in 'soup' variable
soup = bs(r.content, 'html.parser')
# the code 'soup.find()' is trying to find the github profile image by its class and print its URL.
profile_img = soup.find('img', {'class' : 'avatar avatar-user width-full border color-bg-default'})['src']
print(profile_img)