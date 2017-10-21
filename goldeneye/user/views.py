# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request
from flask_login import login_required
from flask_paginate import Pagination, get_page_args
from goldeneye.extensions import db
from goldeneye.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@blueprint.route('/')
@login_required
def members():
    """List members."""
    return render_template('users/members.html')


@blueprint.route('/user_list/', methods=['GET','POST'])
def users():
    page, per_page, offset = get_page_args()
    list_columns = {'id': 'ID', 'username': '登录名称', 'active': '是否激活'}
    query = db.session.query(User)
    username = request.args.get('username', default='')
    if username:
        query = query.filter(User.username == username)
    page_results = query.paginate(page, per_page=per_page)

    pagination = Pagination(page=page, per_page=per_page, total=page_results.total,
                            bs_version=3)
    return render_template('users/user_list.html',
                           list_columns=list_columns,
                           results=page_results.items,
                           username=username,
                           pagination=pagination
                           )
