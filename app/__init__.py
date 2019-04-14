
import os
from flask import render_template, Flask

from instance.config import app_config

config_name = os.getenv('FLASK_CONFIG') or 'development'
app = Flask(__name__, instance_relative_config=True, template_folder='../templates/' , static_folder='../static/', static_url_path='/static')

# app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config[config_name])
app.config.from_pyfile('config.py')



from app.api import home, restaurent_controller, exception_handler, menu_controller, order_controller
from app.entity import entities