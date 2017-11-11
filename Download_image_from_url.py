'''
code to download image by url
'''

import random
import urllib.request

def downloaf_image(url):
    name = str(random.randrange(1, 100)) + ".jpg"
    urllib.request.urlretrieve(url, name)

downloaf_image("https://fthmb.tqn.com/8cdFIfAhwNAdNAJelEebxEhrmTI=/735x0/success-56a9fd1f3df78cf772abee09.jpg")