from flask import Flask, render_template
from flask.globals import request
import model

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def hello():
    sumof_num = 0
    if request.method == "POST":
        number1 = request.form["number1"]
        number2 = request.form["number2"]
        sumof_num = model.sum(number1, number2)

    return render_template("index.html", sum=sumof_num)


if __name__ == "__main__":
    app.run(debug=True)
