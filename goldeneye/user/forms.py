# -*- coding: utf-8 -*-
"""User forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from .models import User


class UserForm(FlaskForm):
    """Register form."""

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Verify password',
                            [DataRequired(), EqualTo('password', message='Passwords must match')])

    active = BooleanField('active', default=True)

    is_admin = BooleanField('is_admin', default=False)

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(UserForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(UserForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append('Username already registered')
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append('Email already registered')
            return False
        return True


class UserSearchForm(FlaskForm):
    username = StringField('账号', default='')
    active = SelectField('是否激活', default='', choices=([('', '全选'), ('1', '激活'), ('0', '未激活')]))
