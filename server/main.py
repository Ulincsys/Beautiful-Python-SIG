from flask import Flask, render_template, request, session

app = Flask("test_app")
app.secret_key = "RandomString_MustChange"

@app.route("/")
def root():
    var = request.args.get("input")
    if var:
        session["my_var"] = var
    return render_template("index.j2", my_var = var)
