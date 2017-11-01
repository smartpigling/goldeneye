# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for, abort
from flask_login import current_user, login_required, login_user, logout_user
from flask_menu import register_menu

from goldeneye.extensions import login_manager, db
from goldeneye.public.forms import LoginForm
from goldeneye.user.forms import UserForm
from goldeneye.user.models import User, Role, Permission
from goldeneye.utils import flash_errors

blueprint = Blueprint('public', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # current_user_perms = []
    # for perm in db.session.query(Permission).join(Role, Permission.roles).\
    #         join(User, Role.users).filter(User.id == current_user.id).distinct():
    #     current_user_perms.append(url_for(perm.slug))
    # return render_template('public/home.html', current_user_perms=current_user_perms)
    current_user_perms = ['/about/','/about1/','/about2/','/about11/','/about12/','la','la1']

    return render_template('public/home.html', current_user_perms=current_user_perms)


@blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('You are logged in.', 'success')
            redirect_url = request.args.get('next') or url_for('login')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('public/login.html', form=form)


@blueprint.route('/logout/')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    """Register new user."""
    form = UserForm(request.form)
    if form.validate_on_submit():
        User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)


@blueprint.route('/about/')
@register_menu(blueprint, '.about', '一级菜单', type='N', cls='fa-edit')
def about():
    return redirect(url_for('public.about'))

