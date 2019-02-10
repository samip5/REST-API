from flask import request
from flask_restplus import Resource
from ..util.dto import TestingDto

api = TestingDto.api


@api.route('/')
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello, World!"}
