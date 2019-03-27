from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template('index.html')


@app.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

if __name__ == '__main__':
    app.run(debug=True,
            port=8000)
