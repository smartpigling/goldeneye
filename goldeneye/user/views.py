# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@blueprint.route('/')
@login_required
def members():
    """List members."""
    return render_template('users/members.html')


@blueprint.route('/user_list/')
def users():
    list_columns = [('id','ID'),('username','名称')]
    return render_template('users/list.html', list_columns = list_columns, data = None)
