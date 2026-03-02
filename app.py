from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

registered_emails = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form['email']

        if email in registered_emails:
            return "Email already registered!"

        registered_emails.append(email)
        return redirect(url_for('success'))

    return render_template('index.html')


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
    