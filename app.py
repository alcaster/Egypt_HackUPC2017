from flask import Flask

CONFIG = {
    "TEMPLATES_AUTO_RELOAD": True,
    "SECRET_KEY":12345
}

app = Flask(__name__, static_url_path='/static')
app.config.update(CONFIG)

from views import *
