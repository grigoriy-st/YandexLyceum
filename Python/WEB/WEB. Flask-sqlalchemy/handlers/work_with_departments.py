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
    """ Добавление департамента. """
    ...


@work_with_departments_bp.route('/list_of_departments')
def get_list_of_departments():
    """ Отображение списка департаментов. """
    db_ss = db_session.create_session()
    all_deps = db_ss.query(Department).all()
    current_user_id = current_user.id

    return render_template('list_of_departments.html',
                           departments=all_deps,
                           current_user_id=current_user_id)


@work_with_departments_bp.route('/edit_department/<int:dep_id>')
def edit_department(dep_id):
    """ Редактирование данные департамента. """
    ...


@work_with_departments_bp.route('/delete_department/<int:dep_id>')
def delete_department(dep_id):
    """ Удаление департамента. """
    ...
