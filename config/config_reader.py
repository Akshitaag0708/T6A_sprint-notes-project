import os
import yaml


class ConfigReader:

    @staticmethod
    def read_config():
        path = os.path.join(os.path.dirname(__file__) , "env.yaml")

        with open(path, "r") as file:
            return yaml.safe_load(file)