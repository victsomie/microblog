from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)#lets the user to choose if cookies can be iinstalld in their browsers so that they are remembered when they come back



    """
    We imported the Form class, and the two form field classes that we need, StringField and BooleanField.

The DataRequired import is a validator, a function that can be attached to a field to perform validation on the data submitted by the user. The DataRequired validator simply checks that the field is not submitted empty.
    """
