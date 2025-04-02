# import logging as logger 
from Utils import LoggerUtility
logger = LoggerUtility.setup_logger('Flask')
# from Utils import LoggerFactory
# logger = LoggerFactory.create(name='Flask')

# import logging as logger

from .BaseController import BaseController
from Repositories.TaskRepository import TaskRepository
from flask import Blueprint, request

class TaskController(BaseController):
    def __init__(self, taskRepository: TaskRepository):
        self.TaskControllerBP = Blueprint('TaskController', __name__)
        self.taskRepository = taskRepository
        self.register_routers()
        

    def register_routers(self):
        self.TaskControllerBP.add_url_rule('/task/all', 'get_all_tasks', self.get_all_tasks, methods=['GET'])
        self.TaskControllerBP.add_url_rule('/task/add', 'add_task', self.add_task, methods=['POST'])

    # @TaskControllerBP.route('/tasks/all',methods=['GET'])
    def get_all_tasks(self):
        logger.info('Getting all tasks')
        result = self.taskRepository.get_all()
        return "get_all_tasks"
    
    def add_task(self):
        form = request.form
        logger.info(f'Adding a new task {form['text']} with status {form['done']}')
        text: str = form['text']
        done: bool = bool(form['done'])
        task = self.taskRepository.add_task(text=text, done=done)
        logger.info('New task')
        logger.info(task)
        return "add_task"
    


# self.flask_app.route(self.route_name,method=['GET'])(self.get_data)
# self.flask_app.route(self.route_name,method=['POST'])(self.write_data)
# self.flask_app.route(self.route_name,method=['DELTE'])(self.delete_data)
