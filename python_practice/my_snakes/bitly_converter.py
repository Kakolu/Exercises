import bitly_api
import sys
from keys import keys

class BitlyConverter:

    def convert(self, url):
        bitly = bitly_api.Connection(access_token=keys['BITLY_AUTH_TOKEN'])
        converted_url = bitly.shorten(url)
        return converted_url['url'];