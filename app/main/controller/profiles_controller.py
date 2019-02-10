from flask import request
from flask_restplus import Resource

from ..util.dto import ProfilesDto
from ..service.profiles_service import get_profile, get_count_by_city, get_cities, getEtunimi, getSukunimi,\
    getEmail, checkPaikkakunta, postUpdateCity, postNewCity

api = ProfilesDto.api
_profile = ProfilesDto.profile


@api.route('')
class Profile(Resource):
    @api.doc('Users profile', responses={200: 'Accepted', 204: 'No Content'})
    @api.param('user_id', 'The user identifier')
    def get(self):
        user_id = request.args.get('user_id')
        """List of profiles"""
        return get_profile(user_id)


@api.route('/countByCity')
class ProfilecountByCity(Resource):
    @api.doc('Get count by city from user profiles')
    def get(self):
        """Count list of cities"""
        return get_count_by_city()


@api.route('/getCities')
class ProfileGetCities(Resource):
    @api.doc('Get cities')
    def get(self):
        """List of cities"""
        return get_cities()


@api.route('/getEtunimi')
class ProfileGetEtunimi(Resource):
    @api.doc("Get user's first name", responses={200: 'Accepted', 204: 'No Content'})
    @api.param('user_id', 'The user identifier')
    def get(self):
        user_id = request.args.get('user_id')
        """Returns the first name"""
        return getEtunimi(user_id)


@api.route('/getSukunimi')
class ProfileGetSukunimi(Resource):
    @api.doc("Get user's last name", responses={200: 'Accepted', 204: 'No Content'})
    @api.param('user_id', 'The user identifier')
    def get(self):
        user_id = request.args.get('user_id')
        """Returns the last name"""
        return getSukunimi(user_id)


@api.route('/getEmail')
class ProfileGetEmail(Resource):
    @api.doc("Get user's email address", responses={200: 'Accepted', 204: 'No Content'})
    @api.param('user_id', 'The user identifier')
    def get(self):
        user_id = request.args.get('user_id')
        """Returns the email address of a user"""
        return getEmail(user_id)


@api.route('/checkPaikkakunta')
class ProfileCheckPaikkakunta(Resource):
    @api.doc("Checks if user has a city listed", responses={200: 'Accepted', 204: 'No Content'})
    @api.param('user_id', 'The user identifier')
    def get(self):
        user_id = request.args.get('user_id')
        return checkPaikkakunta(user_id)


@api.route('/updateCity')
class ProfilePostUpdatePaikkakunta(Resource):
    @api.doc("Update's users city", responses={200: 'Accepted'})
    @api.param('id', 'The setting ID')
    @api.param('user_id', 'The user identfier')
    @api.param('settings_value', 'The setting value to set to')
    def post(self):
        id = request.args.get('id')
        user_id = request.args.get('user_id')
        settings_value = request.args.get('settings_value')
        return postUpdateCity(id, user_id, settings_value)


@api.route('/setCity')
class ProfileSetPaikkakunta(Resource):
    @api.doc("Insert's users city to their profile")
    @api.param('id', 'The setting ID')
    @api.param('user_id', 'The user identfier')
    @api.param('settings_value', 'The setting value to set to')
    def post(self):
        id = request.args.get('id')
        user_id = request.args.get('user_id')
        settings_value = request.args.get('settings_value')
        return postNewCity(id, user_id, settings_value)
