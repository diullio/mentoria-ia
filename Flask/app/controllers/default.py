from flask import render_template, redirect, current_app, flash, url_for
from app import app


#Flask
from app.models.forms import FormsTeste

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = FormsTeste()

    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data

        print(nome, email, password, confirm_password)
        return redirect(url_for('home'))
    
    return render_template('home.html', form = form)

