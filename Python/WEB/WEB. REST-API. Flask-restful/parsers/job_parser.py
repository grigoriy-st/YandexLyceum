from flask_restful.reqparse import RequestParser


def create_job_parser():
    parser = RequestParser()
    parser.add_argument('jobs_id')
    parser.add_argument('author')
    parser.add_argument('team_leader')
    parser.add_argument('job_title')
    parser.add_argument('work_size')
    parser.add_argument('collaborators')

    return parser

job_parser = create_job_parser()