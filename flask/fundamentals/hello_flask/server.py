from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html", phrase="hello", times=5)

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def hello(name):
    if type(name) == str:
        return "Hi " + name + "!"
    
@app.route('/repeat/<num>/<word>')
def repeat(num,word):
    num=int(num)
    if type(num)==int and type(word)==str:
        return word*num


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

