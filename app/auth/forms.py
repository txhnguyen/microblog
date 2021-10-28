from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User


class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    gender = SelectField(_l('Gender'),
        choices=[
            (None, ""),
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
        validators=[DataRequired()],
    )
    education = SelectField(_l('Highest completed education'),
        choices=[
            (None, ""),
            ("Primary education", "Primary education"),
            ("High school diploma", "High school diploma"),
            (
                "Vocational education",
                "Vocational education (e.g. hair stylist, electrician, plumber)",
            ),
            ("University bachelor degree", "University bachelor degree"),
            ("5-year university degree, PhD ", "5-year university degree or PhD"),
        ],
        validators=[DataRequired()],
    )
    background = SelectField(_l('Background knowledge and skills in...'),
        choices=[
            (None, ""),
            ("Information systems", "Information systems"),
            ("Customer service", "Customer service"),
            ("Sales and marketing", "Sales and marketing"),
            ("Engineering, R&D", "Engineering, R&D"),
            ("Purchasing/procurement", "Purchasing/procurement"),
            (
                "Operations, administrations, manufacturing",
                "Operations, administrations or manufacturing",
            ),
            ("Consultancy", "Consultancy"),
            ("HR/personnel", "HR/personnel"),
            ("General management", "General management"),
            ("Creative sector", "Creative sector"),
        ],
        validators=[DataRequired()],
    )
    generation = SelectField(_l('Age'),
        choices=[
            (None, ""),
            ("Generation Z", "18 - 24"),
            ("Milennials", "25 - 40"),
            ("Generation X", "41 - 56"),
            ("Boomers", "57 - 75"),
            ("Greatest Generation", "76 - 93"),
        ],
        validators=[DataRequired()],
    )
    zone = SelectField(_l('Zone'),
        choices=[
            (None, ""),
            ("European", "Europe"),
            (
                "North African, Middle Eastern or Central Asian",
                "North Africa, Middle Eastern or Central Asian",
            ),
            ("Sub-Saharan African", "Sub-Sahara Africa"),
            ("South and South-East Asian", "South or South-East Asia"),
            ("East Asian", "East Asia"),
            ("Latin American", "South-America"),
            ("Carribean", "Carribean"),
            (
                "North-American and Australasian",
                "North-America, Australia or New-Zealand",
            ),
        ],
        validators=[DataRequired()],
    )
    region = SelectField("Region", choices=[], validators=[DataRequired()])
    ethnicity = SelectField(_l('Ethnicity (which suits best)'),
        choices=[
            (None, ""),
            ("white", "White"),
            ("black", "Black"),
            ("latino", "Latino"),
            ("asian", "Asian"),
        ],
        validators=[DataRequired()],
    )

    phone = SelectField(_l('I am completing this task on my phone.'),
        choices=[
            (None, ""),
            ("phone", "Yes"),
            ("not a phone", "No"),
        ],
        validators=[DataRequired()],
    )
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    # email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    # password = PasswordField(_l('Password'), validators=[DataRequired()])
    # password2 = PasswordField(
    #     _l('Repeat Password'), validators=[DataRequired(),
    #                                        EqualTo('password')])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different email address.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))



