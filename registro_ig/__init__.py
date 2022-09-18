from flask import Flask

app = Flask(__name__)

from registro_ig.routes import *