
from flask import Flask, request
from werkzeug.utils import secure_filename
from helper import classify_loan
import json 
import pandas as pd
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
<html>
<head><title>Marketing Model Prediction</title></head><body>
<h1>Enter data to see Model prediction</h1>
      <form action = "/uploader" method = "POST">
          age: <input name="age"/>
          <br/><br/>
          job: <input name="job"/>
          <br/><br/>
          marital: <input name="marital"/>
          <br/><br/>
          education: <input name="education"/>
          <br/><br/>
          default: <input name="default"/>
          <br/><br/>
          balance: <input name="balance"/>
          <br/><br/>
          housing: <input name="housing"/>
          <br/><br/>
          loan: <input name="loan"/>
          <br/><br/>
          contact: <input name="contact"/>
          <br/><br/>
          day: <input name="day"/>
          <br/><br/>
          month: <input name="month"/>
          <br/><br/>
          duration <input name="duration"/>
          <br/><br/>
          campaign: <input name="campaign"/>
          <br/><br/>
          pdays <input name="pdays"/>
          <br/><br/>
          previous: <input name="previous"/>
          <br/><br/>
          poutcome <input name="poutcome"/>
          <br/><br/>
          <button type="submit">Submit</button>
        </form>   
</body>
</html>
"""

@app.route("/uploader", methods = ['POST'])
def classify():
    
    test_val['age'] = int(request.form["age"])
    test_val['job'] = request.form["job"]
    test_val['marital'] = request.form["marital"]
    test_val['education'] = request.form["education"]
    test_val['default'] = request.form["default"]
    
    test_val['balance'] = int(request.form["balance"])
    test_val['housing'] = request.form["housing"]
    test_val['loan'] = request.form["loan"]
    test_val['contact'] = request.form["contact"]
    test_val['day'] = int(request.form["day"])
    
    test_val['month'] = request.form["month"]
    test_val['duration'] = int(request.form["duration"])
    test_val['campaign'] = int(request.form["campaign"])
    test_val['pdays'] = int(request.form["pdays"])
    test_val['previous'] = int(request.form["previous"])
    test_val['poutcome'] = request.form["poutcome"]
    
    print("value passed :", test_val)
    #results = classify_loan(json.dumps(test_val))
    results = classify_loan(test_val)
    return f"""
<html>
<head><title>Marketing Model Prediction</title></head>
<body>
<h1>Result from your data: {results}</h1>
<pre>
Full data:
{results}
</pre>
</body>
</html>
"""
