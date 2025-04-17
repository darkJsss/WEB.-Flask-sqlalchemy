from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField, BooleanField, StringField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, EqualTo, InputRequired
from data.models.users_model import User
from wtforms.validators import DataRequired, Email, Length, EqualTo
from data.db_session import create_session

class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email(message="Некорректный адрес электронной почты.")])
    password = PasswordField('Пароль', validators=[
        DataRequired(),
        Length(min=6, max=128, message="Длина пароля должна составлять минимум 6 символов."),
        EqualTo('confirm_password', message="Пароли не совпадают")
    ])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

    def validate_email(self, field):
        session = create_session()
        existing_user = session.query(User).filter(User.email == field.data).first()
        if existing_user:
            raise ValidationError('Такой email уже зарегистрирован.')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class AddWorkForm(FlaskForm):
    job_title = StringField('Название работы', validators=[InputRequired(), Length(max=100)])
    description = TextAreaField('Описание работы', validators=[Length(max=500)])
    submit = SubmitField('Добавить работу')

class EditWorkForm(FlaskForm):
    job_title = StringField('Название работы', validators=[InputRequired(), Length(max=100)])
    description = TextAreaField('Описание работы', validators=[Length(max=500)])
    submit = SubmitField('Обновить работу')