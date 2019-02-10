from flask_restplus import Api
from flask import Blueprint

from .main.controller.api_user_controller import api as api_user_ns
from .main.controller.profiles_controller import api as profiles_ns
from .main.controller.hello_controller import api as testing_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Messis API',
          version='1.0'
          )

api.add_namespace(api_user_ns, path='/api_user')
api.add_namespace(testing_ns, path='/Hello')
api.add_namespace(profiles_ns, path='/profiles')