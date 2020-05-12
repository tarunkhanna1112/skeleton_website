#btn btn-success btn-block
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
	search1 = StringField('',render_kw={ "placeholder": "  search..."}, id="searchspace")
	submit1 = SubmitField('Search',render_kw={"class": "btn btn-success btn-block", "fontsize":"60px"}, id="submitfield")

class SearchForm1(FlaskForm):
	submit2 = SubmitField('previous',render_kw={"class": "btn btn-success"}, id="submitfield1")
	submit3 = SubmitField('next',render_kw={"class": "btn btn-success"}, id="submitfield1")