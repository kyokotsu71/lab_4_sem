from flask import Flask, render_template
from schema import factory, Story


app = Flask(__name__)


@app.route("/show-form")
def show_form():
    return render_template('OurForm.html')
@app.route("/show-questions", methods=['POST'])
def show_results():
    print(request.form)
    return "OK"


if __name__ == "__main__":
    session = factory()
    app.run(host="127.0.0.1", port=4321)
