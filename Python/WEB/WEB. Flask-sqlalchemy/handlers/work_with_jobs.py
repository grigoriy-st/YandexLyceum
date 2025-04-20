import datetime
from datetime import datetime

from flask import (Blueprint, render_template,
                   redirect, request, abort,
                   url_for, flash, get_flashed_messages
                   )
from flask_login import login_user, logout_user, login_required, current_user

from data import db_session
from data.users import User
from data.jobs import Jobs
from data.hazard_category import HazardCategory

from sqlalchemy.exc import IntegrityError

work_with_jobs_bp = Blueprint('work_with_jobs', __name__)


@work_with_jobs_bp.route('/create_job', methods=['GET', 'POST'])
@login_required
def create_job():
    """ Страница добавления работы. """

    db_ss = db_session.create_session()

    # Получение всех пользователей
    team_leaders = db_ss.query(User).all()
    current_user_id = current_user.id

    if request.method == 'POST':
        job_title = request.form['job_title']
        team_leader = request.form['team_leader']
        beginning_of_duration = request.form['beginning_of_duration']
        end_of_duration = request.form['end_of_duration']
        collaborators = request.form['collaborators']
        is_finished = request.form['is_finished']
        hazard_category = request.form['hazard_category']

        # Вычисление разницы времени
        start_date = datetime.strptime(beginning_of_duration, "%Y-%m-%dT%H:%M")
        end_date = datetime.strptime(end_of_duration, "%Y-%m-%dT%H:%M")
        difference = end_date - start_date
        days_difference = difference.days
        seconds_difference = difference.seconds

        work_size = days_difference * 24 + seconds_difference // 3600

        new_job = Jobs(
            author=current_user_id,
            team_leader=team_leader,
            job_title=job_title,
            collaborators=collaborators,
            start_date=start_date,
            end_date=end_date,
            work_size=work_size,
            is_finished=True if is_finished == "finished" else False,
            hazard_category=hazard_category,
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

    hazard_category = db_ss.query(HazardCategory).all()

    return render_template('new_job.html', current_user_id=current_user_id,
                           team_leaders=team_leaders,
                           hazard_category=hazard_category)


@work_with_jobs_bp.route('/jobs_list')
@login_required
def get_jobs_list():
    """ Отображение списка работ. """

    db_ss = db_session.create_session()
    jobs = db_ss.query(Jobs).all()
    current_user_id = current_user.id
    message = get_flashed_messages()
    # print(message)

    return render_template('jobs.html', jobs=jobs,
                           current_user_id=current_user_id,
                           message=message)


@work_with_jobs_bp.route('/delete_job/<int:job_id>', methods=['GET', 'POST'])
def delete_job(job_id):
    """ Удаление работы. """

    db_ss = db_session.create_session()
    job = db_ss.query(Jobs).filter(Jobs.id == job_id).first()
    db_ss.delete(job)
    db_ss.commit()

    message = f'Работа \"{job.job_title}\" с id={job.id} удалена!'
    flash(message)

    return redirect(url_for('work_with_jobs.get_jobs_list'))


@work_with_jobs_bp.route('/edit_job/<int:job_id>', methods=['GET', 'POST'])
def edit_job(job_id):
    """ Редактирование работы. """

    db_ss = db_session.create_session()
    job = db_ss.query(Jobs).filter(Jobs.id == job_id).first()
    users = db_ss.query(User).all()
    hazard_category = db_ss.query(HazardCategory).all()

    if request.method == 'POST':
        job.job_title = request.form.get('job_title')
        job.team_leader = request.form.get('team_leader')
        job.work_size = request.form.get('work_size')
        job.collaborators = request.form.get('collaborators')
        job.is_finished = True if request.form.get('is_finished') == 'on' else False
        job.hazard_category = request.form.get('hazard_category')

        db_ss.commit()
        message = f'Запись по работе \"{job.job_title}\" c id={job_id} изменена!'

        flash(message)

        return redirect(url_for('work_with_jobs.get_jobs_list'))

    return render_template('job_for_editing.html',
                           job=job,
                           users=users,
                           hazard_category=hazard_category)
