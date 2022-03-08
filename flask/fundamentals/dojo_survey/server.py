from flask import Flask, render_template, request, session, redirect  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "lalalala"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print("Got Post Info")
    print(request.form)
    # Here we add two properties to session to store the name and email
    session['name']= request.form['name']
    session['location']= request.form['location']
    
    if request.form.get("HTML"):
        session['HTML'] = request.form['HTML']
    if request.form.get("Javascript"):
        session['Javascript'] = request.form['Javascript']
    if request.form.get("Python"):
        session['Python'] = request.form['Python']
    session['pizza']= request.form['pizza']
    session['comment']= request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    print(request.form)
    return render_template("result.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect("/")


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

