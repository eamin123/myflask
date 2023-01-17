from werkzeug.wrappers import Request, Response
from flask import Flask, render_template, request

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
        
       # print(request.form["email"])
       # form_data = request.form
        return render_template('data.html',name=name,city=city,country=country)
 
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 9000, app)
    
