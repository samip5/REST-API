from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Messages import MessageResource
from resources.Messages import CountMessages

api_bp = Blueprint('api', __name__)
api = Api(api_bp)



# Route
api.add_resource(Hello, '/Hello')
api.add_resource(MessageResource, '/Messages')
api.add_resource(CountMessages, '/userMessageCount')
