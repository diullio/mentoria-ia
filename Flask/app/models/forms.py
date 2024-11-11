from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, RadioField, DateField, FileField, SelectField, SubmitField, FloatField, ValidationError, PasswordField
from wtforms.validators import DataRequired, Optional, Email, Regexp, EqualTo, Length
from flask_wtf.file import FileAllowed, FileRequired


class FormsTeste(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(),
                                                     Length(min=8, message='A senha deve conter pelo menos 8 caracteres'), Regexp('^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', message='A senha deve conter pelo menos uma letra maiúscula, um número e um caractere especial.')])
    confirm_password = PasswordField('Confirme sua senha', validators=[DataRequired(), EqualTo('password', message='As senhas devem ser iguais')])






    # numero = IntegerField('Numero', validators=[Optional()])
    # dt_validade = DateField('Data de Validade', validators=[Optional()], format='%Y-%m-%d')
    # file = FileField('Arquivo', validators=[FileRequired(), FileAllowed(['pdf'], 'Tipos de arquivos permitidos: PDF')])

