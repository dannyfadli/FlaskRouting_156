from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Halaman login

@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', username=name)  # Halaman sapaan

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')  # Gunakan 'get' untuk menghindari error jika key tidak ada
        if user:
            return redirect(url_for('welcome', name=user))
        else:
            return "Error: Username is required!", 400
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
