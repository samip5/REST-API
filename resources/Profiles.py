from flask import request
from flask_restplus import Resource
from models import db, Profile
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound

import requests as http_client

class ProfilesResource(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        action = request.args.get('action')
        if user_id is not None and action is None:
            query = db.session.query(Profile.settingsid, Profile.settingsvalue)\
                .filter(Profile.userid == user_id)\
                .all()
            return {'status': 'success', 'data': query}, 200
        elif action == str("countByCity"):
            settings_value = int(4)
            query = db.session.query(Profile.settingsvalue, func.count(Profile.settingsvalue))\
                .group_by(Profile.settingsvalue)\
                .filter(Profile.settingsid == settings_value)\
                .all()
            return {'status': 'success', 'data': query}, 200
        elif action == str("cities"):
            settings_value = int(4)
            query = db.session.query(Profile.settingsvalue).distinct()\
                .filter(Profile.settingsid == settings_value)\
                .all()
            return {'status': 'success', 'data': query}, 200
        elif action == str("getEtunimi") and user_id is not None:
            settings_value = int(2)
            query = db.session.query(Profile.settingsvalue)\
                .filter(Profile.userid == user_id)\
                .filter(Profile.settingsid == settings_value)\
                .all()
            return {'status': 'success', 'data': query}, 200
        elif action == str("getSukunimi") and user_id is not None:
            settings_value = int(3)
            query = db.session.query(Profile.settingsvalue) \
                .filter(Profile.userid == user_id) \
                .filter(Profile.settingsid == settings_value) \
                .all()
            return {'status': 'success', 'data': query}, 200
        elif action == str("getEmail") and user_id is not None:
            settings_value = int(1)
            query = db.session.query(Profile.settingsvalue) \
                .filter(Profile.userid == user_id) \
                .filter(Profile.settingsid == settings_value) \
                .all()
            return {'status': 'success', 'data': query}, 200
        elif action == str("checkPaikkakunta") and user_id is not None:
            settings_value = int(4)
            try:
                query = db.session.query(Profile.settingsid).filter(Profile.userid == user_id)\
                    .filter(Profile.settingsid == settings_value).one()
                return {'status': 'success', 'data': query}, 200
            except NoResultFound:
                return {'status': 'failed'}, 400
        else:
            return {'status': 'failed', 'message': 'This is not how it works'}, 400

    def post(self):
        user_id = request.args.get('user_id')
        action = request.args.get('action')
        settings_id = request.args.get('settings_id')
        settings_value = request.args.get('settings_value')
        if user_id is None:
            return {'status': 'failed', 'message': 'This is not how it works, you need to '
                                                   'pass something else too for it to work.'}, 400
        elif action == str("update") and settings_id is not None and user_id is not None and settings_value is not None:
            if settings_id == str(4) or settings_id == str(9):
                # Haetaan kaupunkien/kuntien valkoinen lista avoimen datan API:sta.
                client = http_client.get(f'https://www.avoindata.fi/data/fi/data/api/3/action/datastore_search?q='
                                         f'{settings_value}&resource_id=b1cb9870-191f-4616-9c53-5388b7ca6beb')
                whitelist = client.json()
                for entry in whitelist['result']['records']:
                    if entry['KUNTANIMIFI'] == settings_value:
                        profile = Profile.query.filter_by(userid=user_id, settingsid=settings_id).first()
                        profile.settingsvalue = settings_value
                        db.session.commit()
                    return {'status': 'success'}, 200
                return {'status': 'failed', 'message': "Not accepted."}, 400
        elif action == str("insert_new") and settings_id is not None and user_id is not None \
                and settings_value is not None:
            if settings_id == str(4) or settings_id == str(9):
                client = http_client.get(f'https://www.avoindata.fi/data/fi/data/api/3/action/datastore_search?q='
                                         f'{settings_value}&resource_id=b1cb9870-191f-4616-9c53-5388b7ca6beb')
                whitelist = client.json()
                for entry in whitelist['result']['records']:
                    if entry['KUNTANIMIFI'] == settings_value:
                        profile_add = Profile(user_id, settings_id, settings_value)
                        db.session.add(profile_add)
                        db.session.commit()
                        return {'status': 'success'}, 200
        elif action == str("update") and settings_id is not None:
            return {'status': 'failed', 'message': 'This is not how it works, you need to '
                                                   'pass me settings_value too for it to work.'}, 400
        else:
            return {'status': 'failed'}, 400
