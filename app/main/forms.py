from flask_wtf import FlaskForm
from wtforms import StringField,SelectMultipleField,widgets, TextAreaField, SubmitField
from wtforms.validators import Required,Email



# Subscribe form
class SubscriptionForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    subscribe=StringField('Subscribe')


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label= False)
    option_widget = widgets.CheckboxInput()

class SimpleForm(FlaskForm):
    files = [('18', "Action"),('16', "Animation"),('35', "Comedy"), ('27', "Horror"), ('10749', "Romance"), ('878', 'Sci-fi')]
    example = MultiCheckboxField('Label', choices=files)

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you.',validators = [Required()])
  submit = SubmitField('Submit')