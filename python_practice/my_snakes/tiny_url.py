import tinyurl

class TinyUrlConverter:
    def convert(self, url):
        return tinyurl.create_one(url)