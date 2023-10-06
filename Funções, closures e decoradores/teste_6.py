from flask import Flask

app = Flask(__name__)

'''
Flask acaba usando decorators
'''
@app.route('/')
def index():
    return 'olá Live'

@app.route('/live')
def live_page():
    return 'Estamos online?'

app.run()