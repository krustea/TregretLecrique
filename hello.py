from ledobject import Led

from flask import Flask
app = Flask(__name__)

from flask import render_template
@app.route('/on/')
def hello():
    return render_template('on.html')

@app.route('/on/')
@app.route('/on/<nbr>')
def on(nbr):
    if nbr == '1':
        led1.on(14)
    elif nbr == '2':
        led2.on(15)
    return render_template('on.html', nbr=nbr)

@app.route('/off/')
@app.route('/off/<nbr>')
def off(nbr):
    if nbr == '1':
        led1.off(14)
    elif nbr == '2':
        led2.off(15)
    return render_template('on.html', nbr=nbr)
