#--*--coding: utf-8--*--

from flask import Blueprint, render_template

from app import app


mod = Blueprint('error', __name__)



'''
'''
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/page_system_404.html'), 404

'''
'''
@app.errorhandler(500)
def page_not_found(e):
    return render_template('error/page_system_500.html'), 500 