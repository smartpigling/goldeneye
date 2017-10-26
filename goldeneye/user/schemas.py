from marshmallow import Schema, fields, ValidationError, pre_load


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    active = fields.Bool()


user_schema = UserSchema()
users_schema = UserSchema(many=True)