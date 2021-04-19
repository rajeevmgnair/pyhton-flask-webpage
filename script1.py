from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html") #return "Website Home Page!"

@app.route('/about/')
def about():
    return render_template("about.html")  #return "Website About Page!"

if __name__=="__main__":
    app.run(debug=True)
