from wtforms import Form, StringField, validators

class NameForm(Form):
    firstname = StringField('Firstname', [validators.InputRequired(), validators.Length(min=3, max=60, message='name is too short!'), validators.Regexp(regex="^[a-zA-Z][\sa-zA-Z]*$", message=None)])
    secondname = StringField('Secondname', [validators.InputRequired(), validators.Length(min=3, max=60, message='name is too short!'), validators.Regexp(regex="^[a-zA-Z][\sa-zA-Z]*$", message=None)])