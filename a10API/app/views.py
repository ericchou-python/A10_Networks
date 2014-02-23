from flask import render_template, flash, redirect
from app import app
from forms import LoginForm, ddosForm
import subprocess

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'A10'} #fake user
    posts = [ #fack array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Singapore'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'Welcome to Singapore',
        }
    ]
    return render_template("index.html",
            title = 'Home',
            user=user,
            posts = posts)

@app.route('/ddos', methods = ['GET', 'POST'])
def ddosEnter():
    form = ddosForm()
    if form.validate_on_submit():
        flash('IP requested for Protection= ' + form.dstIP.data)

        # applicable in 2.9.1 with cli.deploy
        f = open('app/scripts/cliDeployCommands.txt', 'w')
        f.write('ddos dst-ip host ' + form.dstIP.data + '\n\n')
        f.close()
        subprocess.call(['python', 'app/scripts/axapi_cli_deploy.py', '-d', '192.168.1.202', '-c', 'app/scripts/cliDeployCommands.txt'])
        return redirect('/ddosResult')
    return render_template('ddos.html',
        title = 'A10 DDoS',
        form = form)

@app.route('/ddosResult')
def ddosResult():
    return render_template("ddosResult.html",
            title = 'A10 DDoS Activated')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])


