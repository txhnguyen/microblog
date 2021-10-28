from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))


class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)


class MessageForm(FlaskForm):
    message = TextAreaField(_l('Message'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))


class AgreementForm(FlaskForm):
    checkbox = BooleanField(
        validators=[
            DataRequired(),
        ],
    )


class SurveyForm(FlaskForm):

    ntb1 = RadioField("If other people don’t seem to accept me, I don’t let it bother me.",
                      choices=[
                          ("1", "Not at all"),
                          ("2", "Sligthly"),
                          ("3", "Moderately"),
                          ("4", "Very"),
                          ("5", "Extremely"),
                      ],
                      validators=[DataRequired()],
   )
    ntb2 = RadioField("I try hard not to do things that will make other people avoid or reject me.",
                      choices=[
                          ("1", "Not at all"),
                          ("2", "Sligthly"),
                          ("3", "Moderately"),
                          ("4", "Very"),
                          ("5", "Extremely"),
                      ],
                      validators=[DataRequired()],
                      )
    ntb3 = RadioField("I seldom worry about whether other people care about me.",
                      choices=[
                          ("1", "Not at all"),
                          ("2", "Sligthly"),
                          ("3", "Moderately"),
                          ("4", "Very"),
                          ("5", "Extremely"),
                      ],
                      validators=[DataRequired()],
                      )
    ntb4 = RadioField("I need to feel that there are people I can turn to in times of need.",
                      choices=[
                          ("1", "Not at all"),
                          ("2", "Sligthly"),
                          ("3", "Moderately"),
                          ("4", "Very"),
                          ("5", "Extremely"),
                      ],
                      validators=[DataRequired()],
                      )
    ntb5 = RadioField("I want other people to accept me.",
                      choices=[
                          ("1", "Not at all"),
                          ("2", "Sligthly"),
                          ("3", "Moderately"),
                          ("4", "Very"),
                          ("5", "Extremely"),
                      ],
                      validators=[DataRequired()],
                      )
    ntb6 = RadioField("I do not like being alone.",
                      choices=[
                          ("1", "Not at all"),
                          ("2", "Sligthly"),
                          ("3", "Moderately"),
                          ("4", "Very"),
                          ("5", "Extremely"),
                      ],
                      validators=[DataRequired()],
                      )
    ntb7 = RadioField("Being apart from my friends for long periods of time does not bother me.",
                      choices=[
                          ("1", "Not at all"),
                          ("2", "Sligthly"),
                          ("3", "Moderately"),
                          ("4", "Very"),
                          ("5", "Extremely"),
                      ],
                      validators=[DataRequired()],
                      )

    ntb8 = RadioField("Being apart from my friends for long periods of time does not bother me.",
                      choices=[
                          ("1", "Not at all"),
                          ("2", "Sligthly"),
                          ("3", "Moderately"),
                          ("4", "Very"),
                          ("5", "Extremely"),
                      ],
                      validators=[DataRequired()],
                      )
    ntb9 = RadioField("It bothers me a great deal when I am not included in other people’s plans.",
                      choices=[
                          ("1", "Not at all"),
                          ("2", "Sligthly"),
                          ("3", "Moderately"),
                          ("4", "Very"),
                          ("5", "Extremely"),
                      ],
                      validators=[DataRequired()],
                      )

    ntb10 = RadioField("My feelings are easily hurt when I feel that others do not accept me.",
                      choices=[
                          ("1", "Not at all"),
                          ("2", "Sligthly"),
                          ("3", "Moderately"),
                          ("4", "Very"),
                          ("5", "Extremely"),
                      ],
                      validators=[DataRequired()],
                      )
    submit = SubmitField("Finalize")