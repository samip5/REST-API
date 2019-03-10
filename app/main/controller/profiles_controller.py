from flask import request
from flask_restplus import Resource, reqparse

from ..util.dto import ProfilesDto
from ..service.profiles_service import get_profile, get_count_by_city, get_cities, get_etunimi, get_sukunimi, \
    get_email, get_birthday_if_consent, get_birthday_bypass_perms, update_permissions, \
    update_sukunimi, post_new_etunimi, post_new_sukunimi, \
    post_update_city, post_new_city, post_new_parrot, get_parrots

api = ProfilesDto.api
_profile = ProfilesDto.profile
_parrot = ProfilesDto.parrot
_profile_update = ProfilesDto.publicity_update_profile

parser = reqparse.RequestParser()
parser.add_argument('Authorization', required=True, type=str, help='Token')


@api.route('/')
class Profile(Resource):
    @api.doc(responses={200: 'Accepted', 204: 'No Content'})
    @api.param('user_id', 'The user identifier')
    @api.expect(parser)
    def get(self):
        """Returns users profile"""
        user_id = request.args.get('user_id')
        """List of profiles"""
        return get_profile(user_id)


@api.route('/countByCity')
class ProfilecountByCity(Resource):
    @api.expect(parser)
    def get(self):
        """Returns count by city from user profiles"""
        return get_count_by_city()


@api.route('/getCities')
class ProfileGetCities(Resource):
    @api.expect(parser)
    def get(self):
        """List of cities"""
        return get_cities()


@api.route('/getEtunimi')
class ProfileGetEtunimi(Resource):
    @api.doc("Get user's first name", responses={200: 'Success', 419: 'Not allowed by user'})
    @api.param('user_id', 'The user identifier')
    @api.expect(parser)
    def get(self):
        """Returns user's first name if allowed"""
        user_id = request.args.get('user_id')
        return get_etunimi(user_id)


@api.route('/getSukunimi')
class ProfileGetSukunimi(Resource):
    @api.doc("Get user's last name", responses={200: 'Success', 419: 'Not allowed by user'})
    @api.param('user_id', 'The user identifier')
    @api.expect(parser)
    def get(self):
        """Returns user's last name if allowed"""
        user_id = request.args.get('user_id')
        return get_sukunimi(user_id)


@api.route('/getEmail')
class ProfileGetEmail(Resource):
    @api.doc("Get user's email address", responses={200: 'Success', 419: 'Not allowed by user'})
    @api.param('user_id', 'The user identifier')
    @api.expect(parser)
    def get(self):
        """Returns the email address of a user if allowed"""
        user_id = request.args.get('user_id')
        return get_email(user_id)


@api.route('/getBirthday')
class ProfileGetBirthday(Resource):
    @api.doc("", responses={200: 'Success', 419: 'Not allowed by user'})
    @api.param('user_id', 'The user identifier')
    @api.expect(parser)
    def get(self):
        """Returns user's birthday if consent is given"""
        user_id = request.args.get('user_id')
        return get_birthday_if_consent(user_id)


@api.route('/getBirthdayBypass')
class ProfileGetBirthdayBypass(Resource):
    @api.doc("", responses={200: 'Success', 204: 'No content'})
    @api.param('user_id', 'The user identifier')
    @api.expect(parser)
    def get(self):
        """Returns user's birthday without checking permissions nor consent"""
        user_id = request.args.get('user_id')
        return get_birthday_bypass_perms(user_id)


@api.route('/getParrots')
class ProfileGetParrots(Resource):
    @api.param('user_id', 'The user identifier')
    @api.expect(parser)
    def get(self):
        """Returns user's parrots."""
        user_id = request.args.get('user_id')
        return get_parrots(user_id)


@api.route('/updateCity')
class ProfilePostUpdatePaikkakunta(Resource):
    @api.doc("Update's users city", responses={200: 'Accepted'})
    @api.param('permission_id', 'The setting ID')
    @api.param('user_id', 'The user identfier')
    @api.param('settings_value', 'The setting value to set to')
    @api.expect(parser)
    def post(self):
        """Updates users city."""
        permission_id = request.args.get('id')
        user_id = request.args.get('user_id')
        settings_value = request.args.get('settings_value')
        return post_update_city(permission_id, user_id, settings_value)


@api.route('/updatePublicityPerms')
class ProfilePostUpdatePerms(Resource):
    @api.expect(_profile_update, parser, validate=True)
    def post(self):
        """Updates specific profile publicity setting"""
        user_id = request.args.get('user_id')
        permisison_id = request.args.get('perm_id')
        settingsid = request.args.get('settings_id')
        permissionvalue = request.args.get('perm_value')
        return update_permissions(user_id, perm_id=permisison_id, settings_id=settingsid,
                                  permissions_value=permissionvalue)


@api.route('/updateLastname')
class ProfileUpdateLastname(Resource):
    @api.param('user_id', 'The user identfier')
    @api.param('lastname', "The users lastname")
    @api.expect(parser)
    def post(self):
        """Insert's users last name to their profile"""
        user_id = request.args.get('user_id')
        lastname = request.args.get('lastname')
        return update_sukunimi(user_id, updatd_lastname=lastname)


@api.route('/setCity')
class ProfileSetPaikkakunta(Resource):
    @api.param('id', 'The setting ID')
    @api.param('user_id', 'The user identfier')
    @api.param('settings_value', 'The setting value to set to')
    @api.expect(parser)
    def post(self):
        """Insert's users city to their profile"""
        permission_id = request.args.get('id')
        user_id = request.args.get('user_id')
        settings_value = request.args.get('settings_value')
        return post_new_city(perm_id=permission_id, user_id=user_id, settings_value=settings_value)


@api.route('/setEtunimi')
class ProfileSetEtunimi(Resource):
    @api.param('user_id', 'The user identfier')
    @api.param('firstname', "The users firstname")
    @api.expect(parser)
    def post(self):
        """Insert's users first name to their profile"""
        user_id = request.args.get('user_id')
        firstname = request.args.get('firstname')
        return post_new_etunimi(user_id, firstname=firstname)


@api.route('/setSukunimi')
class ProfilesSetSukunim(Resource):
    @api.param('user_id', 'The user identfier')
    @api.param('lastname', "The users lastname")
    @api.expect(parser)
    def post(self):
        """Insert's users first name to their profile"""
        user_id = request.args.get('user_id')
        lastname = request.args.get('lastname')
        return post_new_sukunimi(user_id, lastname)


@api.route('/postNewParrot')
class ProfileInsertNewParrot(Resource):
    @api.marshal_list_with(_parrot)
    @api.expect(_parrot, parser, validate=True)
    def post(self):
        """Inserts a new parrot to the database"""
        user_id = request.json.get('user_id')
        message_id = request.json.get('message_id')
        message_date = request.json.get('message_date')
        person_nmae = request.json.get('person_name')
        message_text = request.json.get('message_text')
        message_url = request.json.get('message_url')
        channel_id = request.json.get('channel_id')
        return post_new_parrot(user_id, user_id, message_id, message_date,
                               person_nmae, message_text, message_url, channel_id)
