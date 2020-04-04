import yaml

class configReader:
    __configFilename = "config.txt"

    def readConfig(self):
        with open("config.yaml", "r") as ymlfile:
            cfg = yaml.load(ymlfile)

        print(cfg["input"])
        print(cfg["output"])

        #TODO: cfg["output"]["hpccout"]...

if __name__ == '__main__':
    c = configReader()
    c.readConfig()