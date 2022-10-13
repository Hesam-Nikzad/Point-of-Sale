from flask import Flask, render_template, flash
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
    
    submit_add = SubmitField('اضافه کن')
    submit_del = SubmitField('حذف کن')
    submit_edit = SubmitField('ویرایش کن')
    submit_search = SubmitField('جستجو')

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
    companies = SQL.Show_All_Rows_of_Table('company')

    # Validate the form
    if form.validate_on_submit() and form.submit_add.data:
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
        companies = SQL.Show_All_Rows_of_Table('company')

        flash('اضافه شد')

    elif form.validate_on_submit() and form.submit_del.data:
        name = form.name.data

        form.name.data = ''
        form.phone.data = ''
        form.mobile.data = ''
        form.address.data = ''
        form.city.data = ''
        form.province.data = ''

        SQL.Delete_Row('company', 'name', name)
        companies = SQL.Show_All_Rows_of_Table('company')
        flash('حذف شد')

    elif form.validate_on_submit() and form.submit_edit.data:
        name = form.name.data

        if form.phone.data: 
            SQL.Edit_Row('company', 'name', name, 'phone', form.phone.data)
            form.phone.data = ''

        if form.mobile.data: 
            SQL.Edit_Row('company', 'name', name, 'mobile', form.mobile.data)
            form.mobile.data = ''

        if form.province.data: 
            SQL.Edit_Row('company', 'name', name, 'province', form.province.data)
            form.province.data = ''

        if form.city.data: 
            SQL.Edit_Row('company', 'name', name, 'city', form.city.data)
            form.city.data = ''

        if form.address.data: 
            SQL.Edit_Row('company', 'name', name, 'address', form.address.data)
            form.address.data = ''
        
        form.name.data = ''
        companies = SQL.Show_All_Rows_of_Table('company')
        flash('ویرایش شد')

    elif form.validate_on_submit() and form.submit_search.data:

        companies = SQL.Search('company', 'name', form.name.data)
        form.name.data = ''
    

    return render_template('companies.html',
            companies = companies, 
            name = name,
            form = form)





if __name__ == '__main__':
    print('The Python Flask server is running')
    app.run(port=5000, debug=True)