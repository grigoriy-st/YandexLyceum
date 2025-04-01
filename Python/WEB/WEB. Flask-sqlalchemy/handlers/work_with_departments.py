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
from data.departments import Department

from sqlalchemy.exc import IntegrityError

work_with_departments_bp = Blueprint('work_with_departments', __name__)


@work_with_departments_bp.route('/add_department', methods=['GET', 'POST'])
def add_department():
    """ Добавление отдела. """
    db_ss = db_session.create_session()
    users = db_ss.query(User).all()
    current_user_id = current_user.id

    if request.method == 'POST':
        creator = request.form.get('creator')
        title = request.form.get('title')
        chief = request.form.get('chief')
        members = request.form.get('members')
        print("NOW:", request.form.get('members'))
        dep_email = request.form.get('dep_email')

        new_dep = Department(
            creator=creator,
            title=title,
            chief=chief,
            members=members,
            dep_email=dep_email
        )
        db_ss.add(new_dep)
        db_ss.commit()

        message = f'Отдел с название \"{title}\" добавлен!'
        flash(message)

        return redirect(url_for("work_with_departments.get_list_of_departments"))

    return render_template('add_department.html',
                           users=users,
                           current_user_id=current_user_id)


@work_with_departments_bp.route('/list_of_departments')
def get_list_of_departments():
    """ Отображение списка отделов. """
    db_ss = db_session.create_session()
    all_deps = db_ss.query(Department).all()
    current_user_id = current_user.id

    message = get_flashed_messages()

    return render_template('list_of_departments.html',
                           departments=all_deps,
                           current_user_id=current_user_id,
                           message=message)


@work_with_departments_bp.route('/edit_department/<int:dep_id>', methods=['GET', 'POST'])
def edit_department(dep_id):
    """ Редактирование данных отдела. """
    db_ss = db_session.create_session()
    dep = db_ss.query(Department).filter(Department.id == dep_id).first()
    users = db_ss.query(User).all()

    if request.method == 'POST':
        print(1234)
        dep.title = request.form.get('title')
        dep.chief = request.form.get('chief')
        dep.members = request.form.get('members')
        dep.dep_email = request.form.get('dep_email')
        db_ss.commit()

        message = f'Запись по отделу \"{dep.title}\" изменена!'
        flash(message)

        return redirect(url_for('work_with_departments.get_list_of_departments'))

    return render_template('dep_for_editing.html',
                           users=users,
                           department=dep)


@work_with_departments_bp.route('/delete_department/<int:dep_id>', methods=['GET', 'POST'])
def delete_department(dep_id):
    """ Удаление отдела. """
    db_ss = db_session.create_session()
    dep = db_ss.query(Department).filter(Department.id == dep_id).first()
    db_ss.delete(dep)
    db_ss.commit()

    message = f'Отдел \"{dep.title}\" удалён!'
    flash(message)

    return redirect(url_for('work_with_departments.get_list_of_departments'))
