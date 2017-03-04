from flask import Flask

CONFIG = {
    "TEMPLATES_AUTO_RELOAD": True
}

app = Flask(__name__, static_url_path='/static')
app.config.update(CONFIG)

from views import *
