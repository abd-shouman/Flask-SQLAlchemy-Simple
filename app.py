
from initalizing import before_code_import
before_code_import()

from DI import DI
from Utils import LoggerUtility
logger = LoggerUtility.setup_logger('Flask')    

def start():
    di = DI()
    app = di.app
    return app


if __name__ == '__main__':
    logger.info(f'Main Module triggered {__name__}')
    app = start()
    app.run(host='0.0.0.0', port=5000, threaded=False, debug=False)
    logger.info(f'Flask App closed {__name__}')    
else:
    logger.info(f'Not the main module {__name__}')
    app = start()
    logger.info(f'ELSE | Flask App created {__name__}')