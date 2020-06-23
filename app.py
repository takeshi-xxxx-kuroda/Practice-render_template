# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	#msg = 'Good'
	return render_template('index.html',msg='Good morning')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=80)