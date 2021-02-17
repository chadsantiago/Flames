from wtforms import Form, StringField, validators
from wtforms.validators import ValidationError

class NameForm(Form):
    firstname = StringField('Firstname', [validators.InputRequired(), validators.Regexp(regex="^[a-zA-Z][\sa-zA-Z]*$", message='Invalid character!')])
    secondname = StringField('Secondname', [validators.InputRequired(), validators.Regexp(regex="^[a-zA-Z][\sa-zA-Z]*$", message='Invalid character!')])

    def validate_firstname(self, firstname):
        fname = firstname.data
        fname = fname.replace(" ", "")

        if len(fname) <= 2:
            raise ValidationError('Name must contain at least 3 characters!')
        elif len(fname) >= 20:
            raise ValidationError('Name must not exceed 20 characters!')

    def validate_secondname(self, secondname):
        sname = secondname.data
        sname = sname.replace(" ", "")

        if len(sname) <= 2:
            raise ValidationError('Name must contain at least 3 characters!')
        elif len(sname) >= 20:
            raise ValidationError('Name must not exceed 20 characters!')