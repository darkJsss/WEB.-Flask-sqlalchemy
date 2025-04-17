from flask import Flask, render_template, flash, redirect, request
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from forms import LoginForm, RegisterForm
from data.models.users_model import User
from data.models.work_model import Work
from data.db_session import global_init, create_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandex_lms'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    session = create_session()
    return session.query(User).get(user_id)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        session = create_session()
        new_user = User()
        new_user.email = form.email.data
        new_user.set_password(form.password.data)
        session.add(new_user)
        session.commit()
        flash('Регистрация прошла успешно!', category='success')
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            works = session.query(Work).filter(Work.user_id == current_user.id).all()

            return render_template('home.html', works=works)
        else:
            flash('Неверный логин или пароль.', category='danger')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

if __name__ == '__main__':
    from data.db_session import global_init
    global_init("db/mars_one.sqlite")
    app.run(port=8080, host='127.0.0.1')