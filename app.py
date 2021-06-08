from application import create_app

app = create_app("development")


@app.route("/")
def hello_world():
    return "<p>Hello from Flask!</p>"
