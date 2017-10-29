# -*- coding: utf-8 -*-
"""Admin section, including Role and Permission authorized."""
from flask import Blueprint, flash, redirect, render_template, request, url_for, abort
from flask_login import current_user, login_required, login_user, logout_user
from flask_menu import register_menu

from goldeneye.user.models import User, Role, Permission


blueprint = Blueprint('admin', __name__, url_prefix='/admin', static_folder='../static')


@register_menu(blueprint, '.admin_settings', '系统设置', type='N', cls='fa-gears')
def admin_settings():
    return None


@blueprint.route('/authorized/', methods=['GET', 'POST'])
@register_menu(blueprint, 'admin_settings.authorized', '系统授权', type='M')
def authorized():
    return render_template('admin/authorized.html')