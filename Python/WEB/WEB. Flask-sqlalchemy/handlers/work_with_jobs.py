import datetime
from datetime import datetime

from flask import Blueprint, render_template, redirect, request, abort, url_for
from flask_login import login_user, logout_user, login_required, current_user

from data import db_session
from data.users import User
from data.jobs import Jobs

from sqlalchemy.exc import IntegrityError

work_with_jobs_bp = Blueprint('work_with_jobs', __name__)


@work_with_jobs_bp.route('/create_job', methods=['GET', 'POST'])
def create_job():
    """ Страница добавления работы. """
    db_ss = db_session.create_session()

    # Получение всех пользователей
    team_leaders = db_ss.query(User).all()
    current_user_id = current_user.id

    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        team_leader = request.form['team_leader']
        beginning_of_duration = request.form['beginning_of_duration']
        end_of_duration = request.form['end_of_duration']
        list_of_collaborators = request.form['list_of_collaborators']
        is_finished = request.form['is_finished']

        # Вычисление разницы времени
        start_date = datetime.strptime(beginning_of_duration, "%Y-%m-%dT%H:%M")
        end_date = datetime.strptime(end_of_duration, "%Y-%m-%dT%H:%M")
        difference = end_date - start_date
        days_difference = difference.days
        seconds_difference = difference.seconds

        work_size = days_difference * 24 + seconds_difference // 3600

        new_job = Jobs(
            author=author,
            team_leader=team_leader,
            job=title,
            collaborators=list_of_collaborators,
            start_date=start_date,
            end_date=end_date,
            work_size=work_size,
            is_finished=True if is_finished == "finished" else False,
        )

        # Работа с бд

        try:
            db_ss.add(new_job)
            db_ss.commit()
            message = "Job is added"

        except IntegrityError as e:
            print(f"Error: {e}")
            db_ss.rollback()
            error_message = "Ошибка при добавлении работы. " \
                            "Возможно, такая работа уже существует."

            return render_template('new_job.html',
                                   error=error_message,
                                   team_leaders=team_leaders)

        # return render_template('new_job.html',
        #                        message=message,
        #                        team_leaders=team_leaders)
        return redirect('/jobs_list')

    return render_template('new_job.html', current_user_id=current_user_id,
                           team_leaders=team_leaders)


@work_with_jobs_bp.route('/jobs_list')
@login_required
def get_jobs_list():
    """ Отображение списка работ. """
    db_ss = db_session.create_session()
    jobs = db_ss.query(Jobs).all()
    current_user_id = current_user.id

    return render_template('jobs.html', jobs=jobs,
                           current_user_id=current_user_id)


@work_with_jobs_bp.route('/delete_job', methods=['GET', 'POST'])
def delete_job():
    pass


@work_with_jobs_bp.route('/edit_job/<int:job_id>', methods=['GET', 'POST'])
def edit_job(job_id):
    db_ss = db_session.create_session()
    job = db_ss.query(Jobs).filter(Jobs.id == job_id).first()

    if request.method == 'POST':
        ...
        return redirect('/jobs_list')

    return render_template('job_for_editing.html', job=job)
