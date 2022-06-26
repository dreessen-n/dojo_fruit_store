from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    count = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    now = datetime.now()
    timestamp = now.strftime("%m/%d/%Y %H:%M:%S")
    print(f"Charging {request.form['first_name']} for {count} fruits.")
    print(request.form)
    return render_template("checkout.html", count=count, timestamp=timestamp)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(host='localhost', port=5001, debug=True)