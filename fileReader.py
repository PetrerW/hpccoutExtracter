import os

class fileReader:
    def readLines(self, inputFile):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

        f = open(os.path.join(__location__, inputFile))

        lines = f.readlines()

        for i, line in enumerate(lines):
            lines[i] = lines[i].rstrip("\n")

        return lines

if __name__ == '__main__':
    l = fileReader
    labels = l.readLines(fileReader, "metrics.txt")
    for label in labels:
        print(label)
