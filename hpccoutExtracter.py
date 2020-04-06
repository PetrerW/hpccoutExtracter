import yaml
from extracter import extracter

class hpccoutExctracter:
    def readConfig(self):
        with open("config.yaml", "r") as ymlfile:
            config = yaml.load(ymlfile)

        return config
    
    def extract(self):
        config = self.readConfig()
        e = extracter(config["input"]["metrics"], 
        config["input"]["hpccout"], 
        config["output"]["extract_to"])

        e.saveToCsv()

if __name__ == '__main__':
    h = hpccoutExctracter()
    h.extract()