import json

from flask import Blueprint, Response, abort, request, jsonify
from data import db_session

from data.jobs import Jobs

jobs_api = Blueprint('jobs_api', __name__)


@jobs_api.route('/api/jobs', methods=['GET'])
def get_job_list():

    db_ss = db_session.create_session()
    jobs = db_ss.query(Jobs).all()
    # print(type(jobs))
    # print(jobs[0].job_title)
    jobs_list = []
    for job in jobs:
        jobs_list.append({
            "id": job.id,
            "author": job.author,
            "team_leader": job.team_leader,
            "job_title": job.job_title,
            "work_size": job.work_size,
            "collaborators": job.collaborators,
            "start_date": job.start_date.isoformat() if job.start_date else None,
            "end_date": job.end_date.isoformat() if job.end_date else None,
            "is_finished ": job.is_finished,
        })

    response_data = json.dumps({'jobs': jobs_list})
    return Response(response_data, mimetype='application/json')


@jobs_api.route('/api/jobs', methods=['POST'])
def add_job_by_id():
    job_id = str(request.json['id'])

    if not job_id.isdigit():  # Проверка на некорректную строку
        abort(400)

    required_fields = ['id', 'job_title', 'team_leader_id', 'work_size', 'collaborators']
    if not all(field in request.json for field in required_fields):
        return jsonify({'error': f'Missing required fields. Required: {required_fields}'}), 400


    db_ss = db_session.create_session()
    job = db_ss.query(Jobs).filter(Jobs.id == job_id).first()

    if job:  # Проверка на существующую запись
        return jsonify({'error': 'Job is exists.'})

    new_job = Jobs (
            id=job_id,
            job_title=request.json['job_title'],
            team_leader=request.json['team_leader_id'],
            work_size=request.json['work_size'],
            collaborators=request.json['collaborators'],
            author=request.json.get('author_id', request.json['team_leader_id']),  # Если автор не указан, используем team_leader
            is_finished=request.json.get('is_finished', False),
            hazard_category=request.json.get('hazard_category'),
    )
    respose_data = {
        'job': {
            'status': 'JOB IS ADDED',
            'id': new_job.id,
            'title': new_job.job_title,
            'team_leader_id': new_job.team_leader,
            'work_size': new_job.work_size,
            'is_finished': new_job.is_finished,
        }
    }
    
    try:
        db_ss.add(new_job)
        db_ss.commit()
        message = "Job is added"

    except IntegrityError as e:
        print(f"Error: {e}")
        db_ss.rollback()

    return jsonify(respose_data)


@jobs_api.route('/api/job/<job_id>', methods=['GET'])
def get_job_by_id(job_id):
    if not job_id.isdigit():  # Проверка на некорректную строку
        abort(400)

    db_ss = db_session.create_session()
    job = db_ss.query(Jobs).filter(Jobs.id == job_id).first()

    if not job:  # Проверка на несуществующую запись
        abort(404)

    job = {
            "id": job.id,
            "author": job.author,
            "team_leader": job.team_leader,
            "job_title": job.job_title,
            "work_size": job.work_size,
            "collaborators": job.collaborators,
            "start_date": job.start_date.isoformat() if job.start_date else None,
            "end_date": job.end_date.isoformat() if job.end_date else None,
            "is_finished ": job.is_finished,
    }
    respose_data = json.dumps({'job': job})
    
    return Response(respose_data, mimetype='application/json')