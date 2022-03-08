from flask import Flask, render_template, session, redirect  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "lalalala"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    if not "counter" in session:
        session['counter']=0
    session['counter'] += 1
    return render_template("index.html", counter=session['counter'])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect("/")

@app.route('/plustwo')
def plustwo():
    session['counter'] += 1
    return redirect("/")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

