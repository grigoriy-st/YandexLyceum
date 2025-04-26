from flask_restful.reqparse import RequestParser


def create_job_parser():
    parser = RequestParser()
    parser.add_argument('id', type=int, required=True)
    parser.add_argument('job_title', type=str, required=True)
    parser.add_argument('author', type=int, required=True)
    parser.add_argument('team_leader', type=int, required=True)
    parser.add_argument('work_size', type=int, required=True)
    parser.add_argument('collaborators', type=str)
    parser.add_argument('hazard_category', type=int)

    return parser


job_parser = create_job_parser()
