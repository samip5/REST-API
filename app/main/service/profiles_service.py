from app.main.model.profiles import Profile
from app.main import db
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound

import requests as http_client


def get_profile(user_id):
    query = db.session.query(Profile.settingsid, Profile.settingsvalue)\
        .filter(Profile.userid == user_id)\
        .all()
    if query == []:
        return {'status': 'failed', 'message': "Not found."}, 204
    return query


def get_count_by_city():
    settings_value = int(4)
    query = db.session.query(Profile.settingsvalue, func.count(Profile.settingsvalue)) \
        .group_by(Profile.settingsvalue) \
        .filter(Profile.settingsid == settings_value) \
        .all()
    return query


def get_cities():
    settings_value = int(4)
    query = db.session.query(Profile.settingsvalue).distinct()\
        .filter(Profile.settingsid == settings_value)\
        .all()
    return query


def getEtunimi(user_id):
    settings_value = int(2)
    query = db.session.query(Profile.settingsvalue) \
        .filter(Profile.userid == user_id) \
        .filter(Profile.settingsid == settings_value) \
        .all()
    if query == []:
        return {'status': 'failed', 'message': "Not found."}, 204
    return query


def getSukunimi(user_id):
    settings_value = int(3)
    query = db.session.query(Profile.settingsvalue) \
        .filter(Profile.userid == user_id) \
        .filter(Profile.settingsid == settings_value) \
        .all()
    if query == []:
        return {'status': 'failed', 'message': "Not found."}, 204
    return query


def getEmail(user_id):
    settings_value = int(1)
    query = db.session.query(Profile.settingsvalue) \
        .filter(Profile.userid == user_id) \
        .filter(Profile.settingsid == settings_value) \
        .all()
    if query == []:
        return {'status': 'failed', 'message': "Not found."}, 204
    return query


def checkPaikkakunta(user_id):
    settings_value = int(4)
    try:
        query = db.session.query(Profile.settingsid).filter(Profile.userid == user_id) \
            .filter(Profile.settingsid == settings_value).one()
        return query
    except NoResultFound:
        return {'status': 'failed', 'message': "Not found."}, 204


def postUpdateCity(id, user_id, settings_value):
    if id == str(4) or id == str(9):
        # Haetaan kaupunkien/kuntien valkoinen lista avoimen datan API:sta.
        client = http_client.get(f'https://www.avoindata.fi/data/fi/data/api/3/action/datastore_search?q='
                                 f'{settings_value}&resource_id=b1cb9870-191f-4616-9c53-5388b7ca6beb')
        whitelist = client.json()
        for entry in whitelist['result']['records']:
            if entry['KUNTANIMIFI'] == settings_value:
                profile = Profile.query.filter_by(userid=user_id, settingsid=id).first()
                profile.settingsvalue = settings_value
                db.session.commit()
            return {'status': 'success'}, 200
        return {'status': 'failed', 'message': "Not accepted."}, 400


def postNewCity(id, user_id, settings_value):
    if id == str(4) or id == str(9):
        client = http_client.get(f'https://www.avoindata.fi/data/fi/data/api/3/action/datastore_search?q='
                                 f'{settings_value}&resource_id=b1cb9870-191f-4616-9c53-5388b7ca6beb')
        whitelist = client.json()
        for entry in whitelist['result']['records']:
            if entry['KUNTANIMIFI'] == settings_value:
                profile_add = Profile(user_id, id, settings_value)
                db.session.add(profile_add)
                db.session.commit()
                return {'status': 'success'}, 200
        return {'status': 'failed', 'message': "Not accepted."}, 400
