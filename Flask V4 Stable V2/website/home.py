from flask import Blueprint, render_template

Main_home = Blueprint('Main_home', __name__)

@Main_home.route('/index')
def m_home():
    return render_template("index.html")



