import json
from flask import Blueprint, Response
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

@jobs_api.route('/api/job/<int:job_id>')
def get_job_by_id(job_id):
    db_ss = db_session.create_session()
    job = db_ss.query(Jobs).filter(Jobs.id == job_id).first()
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