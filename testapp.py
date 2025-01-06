from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/slice', methods = ['POST'])
def slice_email():
    email = request.form['email']
    try:
        user_name, domain_name = email.split("@")
        result = {"user_name":user_name, "domain_name":domain_name, "email":email}
        return render_template('index.html', result = result)
    except ValueError:
        result = {"error": "Invalid email address. Please try again."}
        return render_template("index.html", result = result)

if __name__ == "__main__":
    app.run(debug=True)
