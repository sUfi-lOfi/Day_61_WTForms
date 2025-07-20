import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv


load_dotenv("variables.env")


class LoginForm(FlaskForm):
    email = EmailField("Email",validators=[DataRequired()])
    password  = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Submit")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("my_key")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        form.email.data = ""
        form.password.data = ""
        if email == "[The email you want it to be]" and password == "[password you wanna validate]":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)
