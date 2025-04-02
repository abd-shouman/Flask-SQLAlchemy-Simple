import logging 


class LoggerUtility:
    formatter = logging.Formatter('[%(asctime)s] - [%(name)s - %(levelname)s] - [%(processName)s %(threadName)s] - [%(filename)s:%(lineno)s - %(funcName)s() ] -  %(message)s', '%Y/%m/%d %I:%M:%S')
    
    @staticmethod
    def setup_logger(name:str='Flask', level:int=logging.INFO):
        if name == 'root' or name in logging.root.manager.loggerDict.keys():
            return logging.getLogger(name)
        
        commandLineHandler = logging.StreamHandler()  # For logging to the console
        commandLineHandler.setFormatter(LoggerUtility.formatter)   # Apply the formatter to the handler
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(commandLineHandler)
        return logger

    def __init__(self):
        #Default utility
        LoggerUtility.setup_logger()
