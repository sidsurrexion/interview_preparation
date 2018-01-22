import sys
import random


def alphabets():
    alphabet = [str(i) for i in range(10)]
    alphabet.extend([chr(i) for i in range(65+26)])
    alphabet.extend([chr(i) for i in range(97+26)])
    return random.shuffle(alphabet)


def hex_generator(alphabet):
    return ''.join([alphabet[random.randint(len(alphabet) - 1)] for i in range(
        6)])


def get_new_tiny_url(input_url):
    tiny_url = ''
    is_new_hex = False
    while not is_new_hex:
        hexa = hex_generator(characters)
        if hexa not in tinyurl_to_url:
            tinyurl_to_url[hexa] = input_url
            tiny_url = 'http://tinyurl.com/' + hexa
            url_to_tinyurl[input_url] = tiny_url
            is_new_hex = True
    return tiny_url


def convert_url_to_tinyurl(input_url):
    if input_url in url_to_tinyurl:
        return url_to_tinyurl[input_url]
    return get_new_tiny_url(input_url)


url_to_tinyurl = {}
tinyurl_to_url = {}
url = sys.stdin
characters = alphabets()
get_new_tiny_url(url)
