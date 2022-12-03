from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[Email("Некорректный email")])
    psw = PasswordField('Пароль: ', validators=[DataRequired(), Length(min=4, max=100,
                                                                       message='пароль должен быть от 4 до 100 символов')])
    remember = BooleanField('Запомнить', default=False)
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    name = StringField('Имя: ', validators=[Length(min=4, max=100, message='имя от 4 до 100')])
    email = StringField('email', validators=[Email('Некорректный email')])
    psw = PasswordField('Пароль: ', validators=[DataRequired(),
                                                Length(min=4, max=100,
                                                       message='пароль должен быть от 4 до 100 символов')])
    psw2 = PasswordField('Повтор пароля: ', validators=[DataRequired(), EqualTo('psw',
                                                                                message='Пароли не совпадают')])
    submit = SubmitField('Регистрация')
