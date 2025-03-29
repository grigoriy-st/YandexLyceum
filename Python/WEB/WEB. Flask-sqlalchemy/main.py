import sqlalchemy
from flask import Flask
from flask_login import LoginManager, login_user, login_required, logout_user
from data import db_session
from data.users import User
from forms.LoginForm import LoginForm
from flask import render_template, redirect


app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        db_ss = db_session.create_session()
        user = db_ss.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template("login.html",
                               message="Error",
                               form=form)
    return render_template('login.html', title='Authorization', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

if __name__ == '__main__':
    app.run(port='8080', host='127.0.0.1')