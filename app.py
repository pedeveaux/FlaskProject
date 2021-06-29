from application import create_app, register_blueprints

app = create_app("development")
register_blueprints(app)