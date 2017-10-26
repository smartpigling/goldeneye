# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_required
from flask_paginate import Pagination, get_page_args
from flask_menu import register_menu

from goldeneye.extensions import db
from goldeneye.user.models import User
from goldeneye.user.forms import UserForm
from goldeneye.user.schemas import user_schema, users_schema
from goldeneye.utils import flash_errors

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@register_menu(blueprint, '.user_settings', '管理设置', cls='fa-gears')
def user_settings():
    return None


@blueprint.route('/list_user/', methods=['GET'])
@register_menu(blueprint, 'user_settings.list_user', '账号管理')
def list_user():
    page, per_page, offset = get_page_args()
    query = db.session.query(User)
    username = request.args.get('username', default='')
    if username:
        query = query.filter(User.username == username)
    page_results = query.paginate(page, per_page=per_page)

    return render_template('users/list_user.html')


@blueprint.route('/user_table/')
def user_table():
    # startIndex = request.args.get('startIndex', default=1)#起始位置
    # pageSize = request.args.get('pageSize', default=10)#页面大小
    draw = request.args.get('draw', default=1)#第几页
    # orderColumn = request.args.get('orderColumn') #排序列
    # orderDir = request.args.get('orderDir', default='asc') #排序方式
    # #查询
    # username = request.args.get('username', default='')
    print(request.args)
    print(draw)

    print(request.args.get('pages'))
    query = db.session.query(User)
    username = request.args.get('username', default='')
    if username:
        query = query.filter(User.username == username)

    page_results = query.paginate(1, per_page=10)

    # return jsonify({'data': users_schema.dump(page_results.items).data})
    return jsonify({'data': users_schema.dump(query.all()).data,'recordsTotal':10, 'draw':1})



# @blueprint.route('/list_user/', methods=['GET'])
# @register_menu(blueprint, 'user_settings.list_user', '账号管理')
# def list_user():
#     page, per_page, offset = get_page_args()
#     list_columns = {'id': 'ID', 'username': '登录名称', 'active': '是否激活'}
#     query = db.session.query(User)
#     username = request.args.get('username', default='')
#     if username:
#         query = query.filter(User.username == username)
#     page_results = query.paginate(page, per_page=per_page)
#
#     pagination = Pagination(page=page, per_page=per_page, total=page_results.total,
#                             bs_version=3)
#     return render_template('users/list_user.html',
#                            list_columns=list_columns,
#                            results=page_results.items,
#                            username=username,
#                            pagination=pagination
#                            )



@blueprint.route('/create_user/', methods=['GET', 'POST'])
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=form.password.data
                    )
        user.save()
        return redirect(url_for('user.list_user'))
    else:
        flash_errors(form)
    return render_template('users/create_user.html', form=form)
