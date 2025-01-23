from flask import Flask,render_template,request,redirect,url_for,session,flash

app = Flask(__name__)

jobs = [
    {
        'id' : 1,
        'Title' : 'Data Analyst',
        'Location' : 'Bengaluru, India',
        'Salary' : 'Rs. 10,00,000'
    },
    {
        'id' : 2,
        'Title' : 'Data Analyst',
        'Location' : 'Bengaluru, India',
        'Salary' : 'Rs. 10,00,000'
    },
    {
        'id' : 3,
        'Title' : 'Data Analyst',
        'Location' : 'Bengaluru, India'
    },{
        'id' : 4,
        'Title' : 'Data Analyst',
        'Location' : 'Bengaluru, India',
        'Salary' : 'Rs. 10,00,000'
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html",jobs = jobs)


if __name__ == "__main__":
    app.run(host = "0.0.0.0",debug=True)