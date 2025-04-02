from yaml import safe_load

class Config:
    def __init__(self, filename:str="Resources/config.yml"):
        self.filename = filename

        with open(self.filename) as f:
            yaml_dict = safe_load(f)
            self.database_connection_string = yaml_dict['database']['connection_string']
        