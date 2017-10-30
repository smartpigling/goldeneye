# -*- coding: utf-8 -*-
"""Admin section, including Role and Permission authorized."""
from flask import Blueprint, flash, redirect, render_template, request, url_for, abort
from flask_login import current_user, login_required, login_user, logout_user
from flask_menu import register_menu

from goldeneye.extensions import db
from goldeneye.user.models import User, Role, Permission


blueprint = Blueprint('admin', __name__, url_prefix='/admin', static_folder='../static')


@blueprint.route('/admin_settings/')
@register_menu(blueprint, '.admin_settings', '系统设置', type='N', cls='fa-gears')
def admin_settings():
    return None


@blueprint.route('/authorized/', methods=['GET'])
@register_menu(blueprint, 'admin_settings.authorized', '授权查看', type='M')
def authorized():
    roles = db.session.query(Role).all()
    active_rid = request.args.get('active_rid', type=int)
    perms = []
    if active_rid:
        perms =[perm.slug for perm in db.session.query(Permission).join(Role, Permission.roles).filter(Role.id==active_rid).all()]
    return render_template('admin/authorized.html',
                           active_rid = active_rid,
                           roles=roles,
                           perms=perms)


@blueprint.route('/save_authorized/', methods=['GET'])
@register_menu(blueprint, 'admin_settings.authorized.save_authorized', '权限设置', type='B')
def save_authorized():
    selected_role = request.form.get('selected_role', type=int)
    perms = request.request.form.getlist('perms')

    return redirect(url_for('admin.authorized', selected_role))