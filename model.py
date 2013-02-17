#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime

from db import db


class Mutter(db.Model):
    __tablename__ = 'mutter'

    mid = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    text = db.Column(db.String(70))

    def __init__(self, timestamp, text):
        self.timestamp = timestamp
        self.text = text

    def __repr__(self):
        return '<Mutter>(%s, %s)' % (self.timestamp, self.text)


def get_mutters():
    return Mutter.query.order_by(Mutter.timestamp.desc()).all()


def set_mutter(text):
    db.session.add(Mutter(datetime.datetime.now(), text))
    db.session.commit()
