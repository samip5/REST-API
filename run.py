from flask import Flask


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/')

    from models import db
    db.init_app(app)

    return app

app = create_app("config")

if __name__ == "__main__":
    #app = create_app("config")
    app.run(host='0.0.0.0', debug=False)
