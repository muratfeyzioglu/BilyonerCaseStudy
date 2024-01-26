import configparser

class Config:
    @staticmethod
    def get_base_url():
        config = configparser.ConfigParser()
        config.read("config/config.ini")
        return config.get("API", "base_url")
