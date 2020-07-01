from flask import Flask, Blueprint, render_template, abort
from jinja2 import TemplateNotFound

from App.Admin.user import user
from App.home import home


app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(home)


if __name__ == "__main__":
    app.run(debug=True)
