from flask import Flask, render_template, request
import subprocess
from random import *
h1 = 127
h2 = randint(0,3)
h3 = randint(0,9)
h4 = randint(0,9)
h = (str(h1)+'.'+str(h2)+'.'+str(h3)+'.'+str(h4))
app = Flask(__name__)


@app.route('/')
def home():
	title = 'Command'
	return render_template('home.html',title = title)
	
	
@app.route('/',methods = ["GET","POST"])
def command():
	result = request.form['command']
	cmd = result.lower()
	if cmd == '':
		title = 'Command'
		return render_template('home.html',title = title)
	else:
		try:
			title = 'Command : '+cmd
			output = subprocess.check_output(cmd, shell=True)  # run the command and capture the output
	
			vrai = (output.decode('utf-8'))  # decode the output and print it to the console
			return render_template('home.html',vrai = vrai,title = title)
		except subprocess.CalledProcessError as e:
			ops = (f"Subprocess returned non-zero exit status: {e.returncode}")
			return render_template('home.html',ops = ops)
		except Exception as e:
			error = (f"An error occurred: {str(e)}")
			return render_template('home.html',error = error)
	title = 'Command'
	return render_template('home.html',title = title)

if __name__ == '__main__':
	app.run(host=h,debug = True)