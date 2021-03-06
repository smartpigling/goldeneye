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


@blueprint.route('/save_authorized/', methods=['GET', 'POST'])
@register_menu(blueprint, 'admin_settings.authorized.save_authorized', '权限设置', type='B')
def save_authorized():
    active_rid = request.values.get('active_rid')
    perms = request.values.getlist('perms')

    if active_rid:
        acti_role = Role.get_by_id(active_rid)
        acti_perms = db.session.query(Permission).filter(Permission.slug.in_(perms)).all()
        acti_role.permissions=acti_perms
        acti_role.save()

    return redirect(url_for('admin.authorized', active_rid=active_rid))


@blueprint.route('/save_role/', methods=['POST'])
def save_role():
    role_id = request.values.get('role_id', default=None)
    role_name = request.values.get('role_name')
    if role_id:
        role = Role.get_by_id(role_id)
        role.name = role_name
        role.save()
    else:
        Role.create(name=role_name)
    return redirect(url_for('admin.authorized', active_rid=role_id))


@blueprint.route('/del_role/', methods=['POST'])
def del_role():
    role_id = request.values.get('role_id', default=None)
    if role_id:
        Role.get_by_id(role_id).delete()
    return redirect(url_for('admin.authorized'))