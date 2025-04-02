from Repositories.Connection import Connection
from Models.TaskModel import TaskModel
# import logging as logger
from Utils import LoggerUtility
logger = LoggerUtility.setup_logger('Flask')
# from Utils import LoggerFactory
# logger = LoggerFactory.create(name='Flask')

# import logging as logger

# from Utils import LoggerFactory
# logger = LoggerFactory.create(name='info')

class TaskRepository:
    def __init__(self, connection: Connection):
        logger.info('TaskRepository initated')
        self.connection = connection
        # self.Session = sessionmaker(bind=self.connection.engine)


    def get_all(self):        
        with self.connection.use_session() as my_session:
            tasks = my_session.query(TaskModel).all()
        return tasks
    
    # def add_task(self, task: TaskModel):
    #     with self.connection.use_session() as session:
    #         task = session.add(task)
    #     return task
    
    def add_task(self, text: str, done: bool):
        with self.connection.use_session() as my_session:
            my_session.add(TaskModel(text=text, done=done))
            my_session.commit()
        return 