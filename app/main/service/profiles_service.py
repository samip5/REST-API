from app.main.model.profiles import Profile
from app.main.model.parrots import ParrotModel as Parrot
from app.main import db
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound
from flask import jsonify

import requests as http_client


def get_profile(user_id):
    query = db.session.query(Profile.settingsid, Profile.settingsvalue) \
        .filter(Profile.userid == user_id) \
        .all()
    if not query:
        return {'status': 'failed', 'message': "Not found."}, 204
    return jsonify(status='success', data=query)


def get_count_by_city():
    settings_value = int(4)
    query = db.session.query(Profile.settingsvalue, func.count(Profile.settingsvalue)) \
        .group_by(Profile.settingsvalue) \
        .filter(Profile.settingsid == settings_value) \
        .all()
    return jsonify(status='success', data=query)


def get_cities():
    settings_value = int(4)
    query = db.session.query(Profile.settingsvalue).distinct() \
        .filter(Profile.settingsid == settings_value) \
        .all()
    return query


def get_etunimi(user_id):
    settings_value = int(2)
    permission_value_1 = int(1)
    query = db.session.query(Profile.settingsvalue) \
        .filter(Profile.userid == user_id) \
        .filter(Profile.settingsid == settings_value, Profile.permissionsvalue == permission_value_1) \
        .all()
    if not query:
        return {'status': 'unauthorized', 'message': "Mot allowed."}, 419
    return jsonify(status='success', data=query)


def get_birthday_if_consent(user_id):
    settings_id = int(5)
    query = db.session.query(Profile.settingsvalue) \
        .filter(Profile.userid == user_id) \
        .filter(Profile.settingsid == settings_id, Profile.notify_consent == True) \
        .all()
    if not query:
        return {'status': 'unauthorized', 'message': "Mot allowed."}, 419
    return jsonify(status='success', data=query)


def get_birthday_bypass_perms(user_id):
    settings_id = int(5)
    query = db.session.query(Profile.settingsvalue).filter(Profile.userid == user_id,
                                                           Profile.settingsid == settings_id).all()
    if not query:
        return {'status': 'failed', 'message': "Not found."}, 204
    return jsonify(status='success', data=query)


def get_sukunimi(user_id):
    settings_value = int(3)
    permission_value_2 = int(1)
    query = db.session.query(Profile.settingsvalue) \
        .filter(Profile.userid == user_id) \
        .filter(Profile.settingsid == settings_value, Profile.permissionsvalue == permission_value_2) \
        .all()
    if not query:
        return {'status': 'unauthorized', 'message': "Mot allowed."}, 419
    return jsonify(status='success', data=query)


def get_parrots(user_id):
    query = db.session.query(Parrot.channel_id, Parrot.message_url, Parrot.message_text) \
        .filter(Parrot.user_id == user_id).all()
    if not query:
        return {'status': 'failed'}, 204
    return jsonify(status='success', data=query)


def get_email(user_id):
    settings_value = int(1)
    query = db.session.query(Profile.settingsvalue) \
        .filter(Profile.userid == user_id) \
        .filter(Profile.settingsid == settings_value) \
        .all()
    if not query:
        return {'status': 'unauthorized', 'message': "Mot allowed."}, 419
    return jsonify(status='success', data=query)


def post_update_city(id, user_id, settings_value):
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
            return {'status': 'success'}, 201
        return {'status': 'failed', 'message': "Not accepted."}, 400


def post_new_city(perm_id, user_id, settings_value):
    if perm_id == str(4) or perm_id == str(9):
        client = http_client.get(f'https://www.avoindata.fi/data/fi/data/api/3/action/datastore_search?q='
                                 f'{settings_value}&resource_id=b1cb9870-191f-4616-9c53-5388b7ca6beb')
        whitelist = client.json()
        for entry in whitelist['result']['records']:
            if entry['KUNTANIMIFI'] == settings_value:
                profile_add = Profile(userid=user_id, settingsid=perm_id, settingsvalue=settings_value,
                                      permisisonsid=None, permissionsvalue=None, notify_consent=False)
                db.session.add(profile_add)
                db.session.commit()
                return {'status': 'success'}, 201
        return {'status': 'failed', 'message': "Not accepted."}, 400


def post_new_etunimi(userid, firstname):
    settings_id = int(2)
    perm_id = int(3)
    profile_add = Profile(userid, settingsid=settings_id, settingsvalue=firstname,
                          permisisonsid=perm_id, permissionsvalue=None, notify_consent=False)
    db.session.add(profile_add)
    db.session.commit()
    return {'status': 'success'}, 201


def post_new_sukunimi(userid, lastname):
    settings_id = int(3)
    perm_id = int(3)
    profile_add = Profile(userid, settingsid=settings_id, settingsvalue=lastname,
                          permisisonsid=perm_id, permissionsvalue=None, notify_consent=False)
    db.session.add(profile_add)
    db.session.commit()
    return {'status': 'success'}, 201


def update_sukunimi(user_id, updatd_lastname):
    settings_id = int(3)
    profile = Profile.query.filter_by(userid=user_id, settings_id=settings_id).first()
    profile.settingsvalue = updatd_lastname
    db.session.commit()
    return {'status': 'success'}, 201


def update_permissions(user_id, perm_id, settings_id, permissions_value):
    profile = Profile.query.filter_by(userid=user_id, permissionsid=perm_id, settings_id=settings_id).first()
    profile.permissionsvalue = permissions_value
    db.session.commit()
    return {'status': 'success'}, 201


def post_new_parrot(parrot_id, user_id, message_id, message_date,
                    person_name, message_text, message_url, channel_id):
    if None not in (parrot_id, user_id, message_id, message_date, person_name, message_text, message_url, channel_id):
        parrots_add = Parrot(parrot_id, user_id, message_id, message_date, person_name, message_text, message_url,
                             channel_id)
        db.session.add(parrots_add)
        db.session.commit()
        return {'status': 'failed'}, 201
    else:
        return {'status': 'failed', 'message': "Something went wrong."}, 400
