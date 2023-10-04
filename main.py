from flask import Flask, render_template

app = Flask('app')

@app.route('/')
def sakums():
    return render_template('index.html')

@app.route('/sveiki')
def sveiki():
    return render_template('sveiki.html')


if __name__ == '__main__':
    app.run(threaded=True, port = 5000)
