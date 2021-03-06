# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_required
from flask_paginate import Pagination, get_page_args
from flask_menu import register_menu

from goldeneye.extensions import db
from goldeneye.user.models import User
from goldeneye.user.forms import UserForm, UserSearchForm
from goldeneye.user.schemas import user_schema, users_schema
from goldeneye.utils import flash_errors

blueprint = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@blueprint.route('/user_settings/')
@register_menu(blueprint, '.user_settings', '管理设置', type='N', cls='fa-gears')
def user_settings():
    return None


@blueprint.route('/list_user/', methods=['GET','POST'])
@register_menu(blueprint, 'user_settings.list_user', '账号管理', type='M')
def list_user():
    page, per_page, offset = get_page_args()
    searchForm = UserSearchForm(request.values)

    query = db.session.query(User)
    if searchForm.username.data:
        query = query.filter(User.username == searchForm.username.data)

    if searchForm.active.data:
        query = query.filter(User.active == searchForm.active.data)

    page_results = query.paginate(page, per_page=per_page)

    pagination = Pagination(page=page, per_page=per_page, total=page_results.total,
                            bs_version=3)
    return render_template('users/list_user.html',
                           results=page_results.items,
                           searchForm=searchForm,
                           pagination=pagination
                           )


@blueprint.route('/create_user/', methods=['GET', 'POST'])
@register_menu(blueprint, 'user_settings.list_user.create_user', '添加用户', type='B')
def create_user():
    form = UserForm(request.form)
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



