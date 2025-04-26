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
        job = session.query(Jobs).filter(Jobs.id == int(jobs_id)).first()
        if not job:
            abort(404, message=f"job {jobs_id} not found")
    finally:
        session.close()


class JobsResource(Resource):
    def get(self, id):
        abort_if_job_not_found(id)
        session = db_session.create_session()
        job = session.query(Jobs).filter(Jobs.id == int(id)).first()

        session.close()
        return {
            'job': {
                'id': job.id,
                'author': job.author,
                'team_leader': job.team_leader,
                'job_title': job.job_title,
                'work_size': job.work_size,
                'hazard_category': job.hazard_category,
            }
        }

    def delete(self, id):
        abort_if_job_not_found(id)

        session = db_session.create_session()
        job = session.query(Jobs).filter(Jobs.id == int(id)).first()
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
                    'hazard_category': job.hazard_category,
                })
            return {
                'status': 'OK',
                'jobs': jobs_list,
            }
        except Exception as e:
            return {'status': 'error',
                    'message': str(e)
                    }
        finally:
            session.close()

    def post(self):
        parser = job_parser.create_job_parser()
        args = parser.parse_args()

        necessary_fields = ['id', 'author', 'team_leader', 'work_size']
        for field in necessary_fields:
            if field not in args.keys():
                return {
                    'status': 'error',
                    'message': f'request doesn\'t have field {field}',
                }, 400

        session = db_session.create_session()
        try:
            founded_job = session.query(Jobs).filter(Jobs.id == int(args['id'])).first()
            if founded_job:
                return {
                    'status': 'error',
                    'message': 'Jobs with this ID alredy exists'
                }, 400

            job = Jobs(
                id=int(args['id']),
                author=args['author'],
                team_leader=args['team_leader'],
                job_title=args['job_title'],
                work_size=args['work_size'],
                hazard_category=args['hazard_category'],
            )
            session.add(job)
            session.commit()

            return {
                'status': 'success',
                'id': f'{job.id}',
            }, 201
        except SQLAlchemyError as e:
            session.rollback()
            return {
                'status': 'error',
                'message': str(e),
            }
        finally:
            session.close()

