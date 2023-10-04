from flask import Flask, render_template, request, json

app = Flask('app')

@app.route('/')
def sakums():
    return render_template('index.html')

@app.route('/sveiki', methods=["POST","GET"])
def sveiki():
    if request.method == "POST":
        dati = request.json
        print(dati)
        vardins = dati["cilvekaVards"]
        uzvardins = dati["cilvekaUzvards"]
        print(vardins,uzvardins)
        render_template('sveiki.html', vards = vardins, uzvards = uzvardins)
        return render_template('sveiki.html', vards = vardins, uzvards = uzvardins)
    return render_template('sveiki.html')

if __name__ == '__main__':
    app.run(threaded=True, port = 5000)
