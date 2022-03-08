from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html", row=8, column=8, usercolor1="red", usercolor2="black")

@app.route('/<row>/')
def row(row):
    row=int(row)
    return render_template("index.html", row=row, column=8, usercolor1="red", usercolor2="black")

@app.route('/<row>/<column>')
def rowandcolumn(row,column):
    row=int(row)
    column=int(column)
    return render_template("index.html", row=row, column=column, usercolor1="red", usercolor2="black")

@app.route('/<row>/<column>/<usercolor1>/<usercolor2>')
def colors(row,column,usercolor1,usercolor2):
    row=int(row)
    column=int(column)
    return render_template("index.html", row=row, column=column, usercolor1=usercolor1,usercolor2=usercolor2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

