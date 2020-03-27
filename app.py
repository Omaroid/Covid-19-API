from flask import Flask, request
import json
import os

from refresh import update
from apscheduler.schedulers.background import BackgroundScheduler

port_ = 5000
interval_minutes = 10

app = Flask(__name__)

def sensor():
    update()
    print("Scheduler is alive!")

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',minutes=interval_minutes)
sched.start()

@app.route('/')
def index():
    with open('data.json') as f:
        d = json.load(f)
    return d

@app.route('/confirmed')
def confirmed():
    with open('data.json') as f:
        d = json.load(f)
    return d['confirmed']

@app.route('/deaths')
def deaths():
    with open('data.json') as f:
        d = json.load(f)
    return d['deaths']

@app.route('/recovered')
def recovered():
    with open('data.json') as f:
        d = json.load(f)
    return d['recovered']

@app.route('/latest')
def latest():
    with open('data.json') as f:
        d = json.load(f)
    return d['latest']

@app.route('/updatedAt')
def updatedAt():
    with open('data.json') as f:
        d = json.load(f)
    return d['updatedAt']

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=port_)
