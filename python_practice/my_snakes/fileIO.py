

class FileIO:
    def fileRead(self, file):
        f = open(file)

        text = f.read()
        f.close()
        return text.split()
