from data import db_session
from parsers import job_parser
from flask import jsonify
from models.jobs import Jobs
from flask_restful import abort, Api, Resource

from flask_restful.reqparse import RequestParser
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash


def abort_if_job_not_found(jobs_id):
    try:
        session = db_session.create_session()
        users = session.query(Jobs).filter(Jobs.id == jobs_id).first()
        if not users:
            abort(404, message=f"user {jobs_id} not found")
    finally:
        session.close()

class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_job_not_found(jobs_id)
        session = db_session.create_session()
        job = session.query(Jobs).filter(Jobs.id == jobs_id).first()
        session.close()
        return {
            'job': {
                'id': job.id,
                'author': job.author,
                'team_leader': job.team_leader,
                'job_title': job.job_title,
                'work_size': job.work_size,
            }
        }
    
    def delete(self, jobs_id):
        abort_if_job_not_found(jobs_id)
        session = db_session.create_session()
        job = session.query(Jobs).filter(Jobs.id == jobs_id).first()
        session.delete(job)
        session.commit()
        session.close()
        return {'success': 'OK'}


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        try:
            jobs = session.query(Jobs).all()
            jobs_list = []
            for job in jobs:
                jobs_list.append({
                    'id': job.id,
                    'author': job.author,
                    'team_leader': job.team_leader,
                    'job_title': job.job_title,
                    'work_size': job.work_size,
                })
        except Exception as e:
            return {'status': 'error',
                    'message': str(e)
                    }
        finally:
            session.close()

    def post(self):
        parser = job_parser.create_job_parser()
        args = parser.parse_args()

        session = db_session.create_session()
        try:
            founded_job = session.query(Jobs).filter(Jobs.id == args['jobs_id']).first()
            if founded_job:
                return {
                    'status': 'error',
                    'message': 'Jobs with this ID alredy exists'
                }, 400
            
            job = Jobs(
                id=args['jobs_id'],
                author=args['author'],
                team_leader=args['team_leader'],
                job_title=args['job_title'],
                work_size=args['work_size'],
            )
            session.add(job)
            session.commit()

            return {
                'status': 'success',
                'id': f'{job.id}',
            }
        except SQLAlchemyError as e:
            session.rollback()
            return {
                'status': 'error',
                'message': str(e),
            }
        finally:
            session.close()

