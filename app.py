from flask import Flask, render_template, request, redirect
import os

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

blockData={}

@app.route("/", methods= ["GET", "POST"])
def home():
     return render_template('signup.html')
    
# Create a route '/signup' with methods GET and POST   
@app.route('/signup', methods=['GET', 'POST'])
# Define signup function
def signup():
    # Access global blockData
    global blockData
    # Check if request method is POST
    if request.method == 'POST':



        # Get username, email, password from the signup form in the respective variables
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        # Create a new block with username, email and password 
        blockData = {
        'username': username,
        'email': email,
        'password': password
        }
        
        
        # Use return redirect('/signin') to load signin route
        return redirect('/signin')
    
    # if not POST request the signup page
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    global blockData
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
      
        # Check if blockData's username and password is same as variable username and password
        if blockData['username'] == username and blockData['password'] == password:
                    # return the profile.html and variable block containing blockData
                    return render_template('profile.html', block= blockData)

        return "Invalid credentials!"

    return render_template('signin.html')

    
if __name__ == '__main__':
    app.run(debug = True, port=4000)



