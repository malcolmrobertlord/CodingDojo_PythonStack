from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html", color="blue", times=3)

@app.route('/play/<num>')
def number(num):
    num=int(num)
    return render_template("index.html", color="blue", times=num)


@app.route('/play/<num>/<usercolor>')
def numberandcolor(num,usercolor):
    num=int(num)
    return render_template("index.html", color=usercolor, times=num)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

