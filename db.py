#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://app:app@localhost/myapp?charset=utf8'
db = SQLAlchemy(app)
