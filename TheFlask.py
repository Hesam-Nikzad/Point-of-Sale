from flask import Flask, jsonify, request, render_template
from Backend import SQL_Control
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CompanyForm(FlaskForm):
    name = StringField('اسم فروشنده یا شرکت', validators=[DataRequired()])
    phone = StringField('تلفن')
    mobile = StringField('موبایل')
    address = StringField('آدرس')
    city = StringField('شهر')
    province = StringField('استان')
    
    submit = SubmitField('اعمال تغییرات')

SQL = SQL_Control('root', 'harchi', '127.0.0.1', 'pos')

app = Flask(__name__)
app.config['SECRET_KEY'] = "You Know Nothing"

@app.route('/', methods=['GET'])
def index():
    
    #List_of_Units= SQL.Show_All_Rows_of_Table('unit_of_measure')
    #resp = jsonify(List_of_Units)
    #resp.headers.add('Access-Control-Allow-Origin', '*')

    return render_template('index.html')

@app.route('/company', methods=['GET', 'POST'])
def company():
    name = None
    form = CompanyForm()

    # Validate the form
    if form.validate_on_submit():
        name = form.name.data
        phone = form.phone.data
        mobile = form.mobile.data
        address = form.address.data
        city = form.city.data
        province = form.province.data

        form.name.data = ''
        form.phone.data = ''
        form.mobile.data = ''
        form.address.data = ''
        form.city.data = ''
        form.province.data = ''

        List = [name, phone, mobile, address, city, province]
        SQL.Insert_Auto_Increment('company', List)

    return render_template('companies.html',
            name = name,
            form = form)

if __name__ == '__main__':
    print('The Python Flask server is running')
    app.run(port=50000, debug=True)