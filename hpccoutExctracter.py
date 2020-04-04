import fileReader
import os

class hpccoutExctacter:
    __inputmetricsFilename = "metrics.txt"
    __hpccoutFilename = "hpccout.txt"
    __csvFilename = "extractedMetrics.csv"

    def __init__(self, inputMetricsFilename, hpccoutFilename, csvFilename):
        self.__inputmetricsFilename = inputMetricsFilename
        self.__hpccoutFilename = hpccoutFilename
        self.__csvFilename = csvFilename

    def readOutput(self):
        l = fileReader
        lines = l.fileReader.readLines(fileReader, self.__hpccoutFilename)

        metrics = l.fileReader.readLines(fileReader, self.__inputmetricsFilename)
        metricsMap = {}
        
        for metric in metrics:
            metricsMap[metric] = []

        for line in lines:
            if line.__contains__("Begin of Summary section."):
                for metric in metrics:
                    if line.__contains__(metric):
                        line.split("=")
                        metricsMap[line].__add__(line[1])
                        continue
                    elif lines.__contains__("End of summary section."):
                        break
        
        return metricsMap

    def saveToCsv(self):
        metricsMap = self.readOutput()

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

        f = open(os.path.join(__location__, self.__csvFilename))

        for metric in metricsMap:
            f.write(metric)
            for val in metricsMap[metric]:
                f.write(";")
                f.write(val)
            f.write("\n")
        
        f.close()

if __name__ == '__main__':
    l = hpccoutExctacter("metrics.txt", "hpccout.txt", "extracted.csv")
    lines = l.readOutput()
    for line in lines:
        print(line)