import yaml
from hpccoutExctracter import hpccoutExctacter

class main:
    def readConfig(self):
        with open("config.yaml", "r") as ymlfile:
            config = yaml.load(ymlfile)

        return config
    
    def extract(self):
        config = self.readConfig()
        extracter = hpccoutExctacter(config["input"]["metrics"], 
        config["input"]["hpccout"], 
        config["input"]["extract_to"])

        extracter.saveToCsv()

if __name__ == '__main__':
    main.extract(main)