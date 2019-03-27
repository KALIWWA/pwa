from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def route_index():
    return render_template('index.html')

@app.after_request
def add_header(response):
    expiry_time = datetime.datetime.utcnow() + datetime.timedelta(100)
    modify_time = datetime.datetime.utcnow()
    response.headers["Expires"] = expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")
    response.headers["Last-Modified"] = modify_time.strftime("%a, %d %b %Y %H:%M:%S GMT")
    response.headers["Etag"] = 'jsjfujeffwe87ytybyy'
    return response

if __name__ == '__main__':
    app.run(debug=True,
            port=8000)