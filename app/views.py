

from flask import render_template, request
from app import app

from forms import AddressForm
import yaml
import psycopg2
from pandas import read_sql
from getpass import getpass


#pwd = getpass('password')

with open('./app/config.yml','r') as fin:
  config = yaml.load(fin)



def create_conn(config):
    try:
      con=psycopg2.connect(dbname=config['dbname'], host=config['host'],
                              port=config['port'], user=config['user'],
                             password =config['password'])
   
      return con
    except Exception as err:
        print(err)


@app.route('/')
def main():
    return render_template("index.html",city = '',procedure ='')

@app.route('/', methods =["POST","GET"])
def index():
    con = create_conn(config)
    cur = con.cursor()
    city = request.form['city']
    
    procedure = request.form['procedure']
    query = "select * from hospprocoder where city = \'{}\' and proceduredescription = \'{}\';".format(city,procedure)
    print(query)
    
    cur.execute(query)
    results = cur.fetchall()
    return render_template("index.html",city = city,procedure = procedure,results = results)

#@app.route('/submit', methods=('GET', 'POST'))
#def submit():
    
 #   form = AddressForm()
  #  if form.validate_on_submit():
   #     return redirect('index.html',form =form)
   # return render_template('index.html', form=form)



