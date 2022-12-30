from flask import Flask, render_template, request, jsonify, json

app = Flask(__name__)


@app.route('/data')
def webapi():
    return render_template('data.html')



@app.route('/data/message', methods= ['POST'])
def setDataMessage():
    if request.method == "POST":
        data = {
            'bodyInfo': {
                'height': request.form['height'],
                'weight': request.form['weight']             
            }
        }
        bmi=float(data["bodyInfo"]["weight"])/((float(data["bodyInfo"]["height"])*0.01)**2)
        return jsonify(result=round(bmi, 2))


if __name__ == '__main__':
    app.run()
