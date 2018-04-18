from bitly_converter import BitlyConverter
from tiny_url import TinyUrlConverter
from fileIO import FileIO

def shortenWithBitly(urls):
    shortUrl = BitlyConverter()
    print("Bitly versions are:")
    for url in urls:
        print(url + " -> " + shortUrl.convert(url))

def shortenWithTiny(urls):
    shortUrl = TinyUrlConverter()
    print("Tiny versions are:")
    for url in urls:
        print(url + " -> " + shortUrl.convert(url))

def getUrls(file):
    fileio = FileIO()
    return fileio.fileRead(file)

if __name__ == "__main__":
    urls = getUrls("urls.txt")
    shortenWithBitly(urls)
    shortenWithTiny(urls)
