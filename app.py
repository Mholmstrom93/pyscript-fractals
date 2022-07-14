import flask
from pathlib import Path

app = flask.Flask(__name__)


@app.get('/')
def index():
    return flask.render_template('index.html')


@app.get('/serviceWorker.js')
def worker():
    app.logger.info('serviceWorker.js started')
    js = Path(__file__).parent / 'static' / 'js' / 'serviceWorker.js'
    text = js.read_text()
    resp = flask.make_response(text)
    resp.content_type = 'application/javascript'
    resp.headers['Service-Worker-Allowed'] = '/'
    return resp