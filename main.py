from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary storage for user data (replace with a database in a real application)
users = []

@app.route('/')
def home():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    # Get user input from the form
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # Create a dictionary to store user data
    user_data = {
        'name': name,
        'email': email,
        'password': password
    }

    # Add user data to the list (in a real application, you would store this in a database)
    users.append(user_data)

    # Redirect to a success page or another relevant page
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return 'Sign-up successful!'

if __name__ == '__main__':
    app.run(debug=True)
