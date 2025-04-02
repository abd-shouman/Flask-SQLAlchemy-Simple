from flask import Flask
from Controllers.TaskController import TaskController
from Models.TaskModel import TaskModel, Base
from Repositories.TaskRepository import TaskRepository
from Repositories.Connection import Connection
import logging as logger
from Utils import LoggerUtility
logger = LoggerUtility.setup_logger('Flask')    

class DI:
    def __init__(self):
        self.init_app()
        self.init_models()
        self.establish_db_connection()
        self.create_db_schema()
        self.init_repositories()
        self.init_controllers()
    
    def init_app(self):
        self.app = Flask(__name__, template_folder='views/templates', static_folder='views/static')
        logger.info(f'Flask App created')

    def init_models(self):
        self.TaskModel = TaskModel()
        logger.info(f'Models initiated')
        
    def establish_db_connection(self):
        self.connection = Connection()
        logger.info(f'Database Connection created at {self.connection.engine.url}')

    def create_db_schema(self):
        self.metadata = Base.metadata
        logger.info(f'Metadata created')
        self.metadata.create_all(bind=self.connection.engine) 
        logger.info(f'All tables created.')

        logger.info("dummy query")
        with self.connection.use_session() as session:
            tasks = session.query(TaskModel).all()
        logger.info("dummy query finished")

    def init_repositories(self):
        self.taskRepository = TaskRepository(self.connection)
        logger.info(f'Repos initiated')

    def init_controllers(self):
        self.taskController = TaskController(self.taskRepository)
        self.app.register_blueprint(self.taskController.TaskControllerBP)
        logger.info(f'Controllers initiated + blueprints created')