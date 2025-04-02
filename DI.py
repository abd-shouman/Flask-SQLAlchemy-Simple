from flask import Flask
from Controllers.TaskController import TaskController
from Models.TaskModel import TaskModel, Base
from Repositories.TaskRepository import TaskRepository
from Repositories.Connection import Connection
import logging as logger
from Utils import LoggerUtility
logger = LoggerUtility.setup_logger('Flask')    
# from Utils import LoggerFactory
# logger = LoggerFactory.create(name='Flask')

# import logging as logger

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
        # if connection_string is None: 
        #     self.connection = Connection()
        # else: 
        #     self.connection = Connection(connection_string)

    def create_db_schema(self):
        # with self.app.app_context():
        self.metadata = Base.metadata
        logger.info(f'Metadata created')
        # self.metadata.reflect(bind=self.connection.engine)
        # logger.info(f'available tables loaded. Found {len(self.metadata.tables)}')
        self.metadata.create_all(bind=self.connection.engine) 
        logger.info(f'All tables created.')
        # self.metadata.reflect(bind=self.connection.engine)
        # logger.info(f'available tables loaded. Found {len(self.metadata.tables)}')
        # logger.info(f'available tables loaded. Found {self.metadata.tables}')

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

# from flask import Flask
# from Controllers.TaskController import TaskController
# from Models.TaskModel import TaskModel, Base
# from Repositories.TaskRepository import TaskRepository
# from Repositories.Connection import Connection

# from Utils.LoggerUtility import LoggerUtility
# logger = LoggerUtility.setup_logger('Flask')    

# class DI:
#     def __init__(self):
#         self.init_app()
#         self.init_models()
#         self.establish_db_connection()
#         self.init_repositories()
#         self.init_controllers()
#         self.create_db_schema() # Moved here

    
#     def init_app(self):
#         self.app = Flask(__name__, template_folder='views/templates', static_folder='views/static')
#         logger.info(f'Flask App created')

#     def init_models(self):
#         self.TaskModel = TaskModel()
#         logger.info(f'Models initiated')
        
#     def establish_db_connection(self):
#         self.connection = Connection()
#         logger.info(f'Database Connection created at {self.connection.engine.url}')

#     def create_db_schema(self):
#         with self.app.app_context(): # Added this line
#             self.metadata = Base.metadata
#             logger.info(f'Metadata created')
#             self.metadata.create_all(bind=self.connection.engine) 
#             logger.info(f'All tables created.')
#             logger.info("dummy query")
#             with self.connection.use_session() as session:
#                 tasks = session.query(TaskModel).all()
#             logger.info("dummy query finished")

#     def init_repositories(self):
#         self.taskRepository = TaskRepository(self.connection)
#         logger.info(f'Repos initiated')

#     def init_controllers(self):
#         self.taskController = TaskController(self.taskRepository)
#         self.app.register_blueprint(self.taskController.TaskControllerBP)
#         logger.info(f'Controllers initiated + blueprints created')
