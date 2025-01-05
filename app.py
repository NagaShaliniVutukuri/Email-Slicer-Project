from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def email_slicer():
    result = {}
    if request.method == "POST":
        email = request.form.get("email").strip()
        if "@" in email:
            username, domain = email.split("@")
            result = {"username": username, "domain": domain}
        else:
            result = {"error": "Invalid email address. Please enter a valid email."}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)