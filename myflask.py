from werkzeug.wrappers import Request, Response
from flask import Flask, render_template, request
import csv 
import pandas as pd


app = Flask(__name__)

@app.route("/")

def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    #if request.method == 'GET':
    #    return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        print(request.form["Name"])
        print(request.form["City"])
        print(request.form["Country"])
        name = request.form["Name"]
        city = request.form["City"]
        country = request.form["Country"]
        #country = openmyfile()
       # print(request.form["email"])
       # form_data = request.form
        df = pd.read_csv('ACX-RLI-Query.csv')
        df.to_csv('ACX-RLI-Query.csv', index=None)
        data = pd.read_csv('ACX-RLI-Query.csv')
        data2 = data[data['Synopsis'].str.contains(name,case=False)]
 
        return render_template('data.html',name=name,city=city,country=country, tables=[data2.to_html()],titles=[''])

def openmyfile():
    # opening the CSV file
        with open('ACX-RLI-Query.csv', mode ='r')as file:
            # reading the CSV file
            csvFile = csv.reader(file)
            return csvFile
            # displaying the contents of the CSV file
            #for lines in csvFile:
            #    print(lines)



    
    
    
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)
    
