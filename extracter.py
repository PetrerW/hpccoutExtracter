import fileReader
import os

class extracter:
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

        summary = False
        for line in lines:
            if line.__contains__("Begin of Summary section."):
                summary = True
                continue
            if summary == True:
                for metric in metrics:
                    if line.__contains__(metric):
                        line = line.split("=")
                        metricsMap[line[0]].append(line[1])
                        continue
                    elif line.__contains__("End of summary section."):
                        summary = False
        
        return metricsMap

    def saveToCsv(self):
        metricsMap = self.readOutput()

        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))

        if os.path.isabs(self.__csvFilename):
            filepath = os.path.split(self.__csvFilename)[0]
            os.makedirs(filepath)

        f = open(os.path.join(__location__, self.__csvFilename), 'w+')

        for metric in metricsMap:
            f.write(metric)
            for val in metricsMap[metric]:
                f.write(";")
                f.write(val)
            f.write("\n")
        
        f.close()

if __name__ == '__main__':
    l = extracter("metrics.txt", "hpccout.txt", "extracted.csv")
    lines = l.readOutput()
    for line in lines:
        print(line)