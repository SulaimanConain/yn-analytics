from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # In a real application, you would process the form data here
    # For now, we'll just redirect back to the home page
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 