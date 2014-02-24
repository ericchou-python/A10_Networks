from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

# Login form object
class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)

# ddos dst-ip form object
class ddosForm(Form):
    dstIP = TextField('ip', validators = [Required()])

# directFlow form object
class directFlow(Form):
    srcIP = TextField('srcIP', validators = [Required()])
