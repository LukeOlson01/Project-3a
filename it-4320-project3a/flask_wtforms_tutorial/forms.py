"""Form class declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from datetime import date
from wtforms.fields.html5 import DateField
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length
from datapackage import Package

class StockForm(FlaskForm):
    """Generate Your Graph."""
    
    #THIS IS WHERE YOU WILL IMPLEMENT CODE TO POPULATE THE SYMBOL FIELD WITH STOCK OPTIONS
    def populate_stock_symbol_options():
        package = Package('https://datahub.io/core/nyse-other-listings/datapackage.json')
        resources = []
        stock_symbols = []
        for resource in package.resources:
            if resource.descriptor['datahub']['type'] == 'derived/csv':
                resources.append(resource.read())
        for resource in resources:
            for stock in resource:
                stock_symbol = (stock[0], stock[0])
                stock_symbols.append(stock_symbol)
        return stock_symbols

    symbol = SelectField("Choose Stock Symbol",[DataRequired()],
        choices=populate_stock_symbol_options(),
    )

    chart_type = SelectField("Select Chart Type",[DataRequired()],
        choices=[
            ("1", "1. Bar"),
            ("2", "2. Line"),
        ],
    )

    time_series = SelectField("Select Time Series",[DataRequired()],
        choices=[
            ("1", "1. Intraday"),
            ("2", "2. Daily"),
            ("3", "3. Weekly"),
            ("4", "4. Monthly"),
        ],
    )

    start_date = DateField("Enter Start Date")
    end_date = DateField("Enter End Date")
    submit = SubmitField("Submit")



