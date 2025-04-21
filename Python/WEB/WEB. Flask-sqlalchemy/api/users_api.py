import json
import pytest
import requests

BASE_URL = 'http://localhost:8080/api/users'

from flask import Blueprint, Flask, Response, abort, request, jsonify
from data import db_session

from data.users import User

users_api = Blueprint('users_apu', __name__)

@users_api.route('/api/users', methods=['GET'])
def get_all_users():
    """ Выдача всех пользователей. """

    db_ss = db_session.create_session()
    users = db_ss.query(User).all()

    users_list = []
    for user in users:
        users_list.append({
            'id': user.id,
            'name': user.name,
            'surname': user.surname,
            'position': user.position,
            'speciality': user.speciality,
            'email': user.email,
        })
    response_data = json.dumps({
        'status': 'all users have been recieved', 
        'jobs': users_list})
    return Response(response_data, mimetype='application/json')


@users_api.route('/api/users/<int:id>', methods=['GET'])
def get_info_to_one_user_by_id(id):
    """ Прсомотр информации по одному пользователю. """

    data = request.get_json()

    # if 'id' not in data.keys():
    #     return jsonify({'error': 'missing user id'}), 400

    # user_id = data['id']

    db_ss = db_session.create_session()
    user = db_ss.query(User).filter(User.id == id).first()
    db_ss.close()
    
    if not user:
        return jsonify({'error': 'user was not found'})

    response_of_user = {
        'id': user.id,
        'name': user.name,
        'surname': user.surname,
        'position': user.position,
        'speciality': user.speciality,
        'email': user.email,
    }
    return jsonify({'user': response_of_user})


@users_api.route('/api/users/add', methods=['POST'])
def add_user():
    """ Добавление пользователя. """
    data = request.get_json()

    necуssary_fields = [
        'id',
        'surname',
        'name',
        'age',
        'position',
        'speciality',
        'email',
        'password',
    ]

    for field in data.keys():
        if field not in necуssary_fields:
            return jsonify({'error': 'field not in necessary fields'})

    if 'id' not in data.keys() or 'password' not in data.keys():
        return jsonify({'error': 'missing user id or password'}), 400

    user_id = data['id']

    db_ss = db_session.create_session()
    user = db_ss.query(User).filter(User.id == user_id).first()

    if user:
        return jsonify({'error': 'user with this id was found'})
# ------------------------
# Нужно сделать логику добавления только тех полей, 
# которые указаны в запросе
# ------------------------

    try: 
        new_user = User(
            id=user_id,
            surname=data['surname'],
            name=data['name'],
            age=data['age'],
            position=data['position'],
            speciality=data['speciality'],
            address=data['address'],
            email=data['email'],
        )

        new_user.set_password(data['password'])
        db_ss.add(new_user)
    finally:
        db_ss.commit()
        db_ss.close()
    

@users_api.route('/api/users/delete', methods=['DELETE', 'POST'])
def delete_user():
    data = request.get_json()

    if 'id' not in data.keys():
        return jsonify({'error': 'missing id'}), 400
    
    user_id = data['id']
    
    db_ss = db_session.create_session()
    user = db_ss.query(User).filter(User.id == user_id).first()
    
    if not user:
        db_ss.close()
        return jsonify({'error': 'user was not found'})
    
    db_ss.delete(user)

    return jsonify({'user': 'is deleted'})


@users_api.route('/api/users/edit', methods=['PUT', 'POST'])
def edit_user():
    data = request.get_json()

    necуssary_fields = [
        'id',
        'surname',
        'name',
        'age',
        'position',
        'speciality',
        'email',
    ]

    for field in data.keys():
        if field not in necуssary_fields:
            return jsonify({'error': 'field not in necessary fields'})

    if 'id' not in data.keys():
        return jsonify({'error': 'missing user id or password'}), 400

    user_id = data['id']

    db_ss = db_session.create_session()
    user = db_ss.query(User).filter(User.id == user_id).first()

    for field in data.keys():
        if field == 'password':
            user.set_password(data['password'])
        else:
            setattr(user, field, data[field])

    db_ss.commit()
    db_ss.close() 

    return jsonify({'user': 'updated successfully'})

