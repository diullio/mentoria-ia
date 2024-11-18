from flask import render_template, redirect, current_app, flash, url_for
from app import app, db
from app.models.tables import User

#Flask
from app.models.forms import FormsTeste

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = FormsTeste()
    mensagem = ''
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        novo_usuario = User(nome, password, email) 

        try:
            #adicionar no banco
            db.session.add(novo_usuario)
            db.session.commit()
            mensagem = 'Inserido com sucesso!'

        except:
            db.session.rollback() #reverte as mudancas em caso de erro
            mensagem = 'Erro!'
        
    return render_template('home.html', form = form, mensagem=mensagem)

@app.route('/consulta', methods=['GET', 'POST'])
def consulta():
    form = FormsTeste()
    usuarios = User.query.all()


    return render_template("consulta.html", form = form, usuarios=usuarios)