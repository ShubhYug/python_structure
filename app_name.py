#Project Created By Shubham Sameliya
from flask import  Flask

app = Flask(__name__, template_folder='templates', static_url_path='/static')
# app = Flask(__name__, template_folder='templates')