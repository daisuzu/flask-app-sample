#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, redirect, url_for, request
from flask.ext.wtf import Form, TextField, validators

import model
from db import db

app = Flask(__name__)
db.create_all()


class TextForm(Form):
    text = TextField(u'今何してる?',
                     [validators.Length(min=1, max=70)])


@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()


@app.route('/', methods=('GET', 'POST'))
def index():
    form = TextForm(csrf_enabled=False)
    mutters = model.get_mutters()
    if request.method == 'POST' and form.validate():
        model.set_mutter(form.text.data)
        return redirect(url_for('index'))
    else:
        return render_template('app.html',
                               TITLE='my app',
                               FORM=form,
                               MUTTERS=mutters)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
