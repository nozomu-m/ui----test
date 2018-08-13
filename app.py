#!/usr/bin/env python
#-*- coding: utf-8 -*-

import subprocess

from flask import Flask
from flask import render_template
from flask import request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    hashID = request.json['after']
    branch = request.json['ref']
    repo = request.json['repository']['name']
    project = "{}_{}".format(repo, branch)
    subprocess.Popen(["python3", "./runSelenium.py", hashID, project])
    return ""


if __name__ == "__main__":
    app.run(port=10080)
