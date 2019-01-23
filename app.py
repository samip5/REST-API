from flask import Blueprint
from flask_restful import Api
from resources.Hello import Hello
from resources.Messages import MessageResource
from resources.Messages import CountMessages
from resources.Messages import CountMessagesByChannel
from resources.Profiles import ProfilesResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)



# Routes
api.add_resource(Hello, '/Hello')
api.add_resource(MessageResource, '/Messages')
api.add_resource(ProfilesResource, '/Profiles')
api.add_resource(CountMessages, '/userMessageCount')
api.add_resource(CountMessagesByChannel, '/userMessageCountByChannels')