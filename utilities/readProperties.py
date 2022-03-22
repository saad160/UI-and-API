import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        config.get('common info','baseURL')