from flask import Flask, render_template, request, make_response

answers = {
    "sleep": {"yes": 0, "mb": 0, "no": 0},
    "education": {"yes": 0, "mb": 0, "no": 0},
    "queue": {"yes": 0, "mb": 0, "no": 0}
}

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return "Страница не найдена"


@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def show_questions():
    return render_template('questions.html')


@app.route("/questions_remake", methods=['GET', 'POST'])
def return_to_questions():
    response = make_response(render_template('questions.html'))
    response.set_cookie('voted', 're')
    return response


@app.route("/results", methods=['GET', 'POST'])
def process_information():
    if request.method == 'GET':
        return render_template('answers.html', answers=answers)
    if request.method == 'POST':
        if 'voted' in request.cookies and request.cookies['voted'] == 'ok':
            return render_template('warning.html')
        else:
            if 'sleep' in request.form:
                if request.form['sleep'] == 'yes':
                    answers['sleep']['yes'] += 1
                if request.form['sleep'] == 'no':
                    answers['sleep']['no'] += 1
                if request.form['sleep'] == 'mb':
                    answers['sleep']['mb'] += 1

            if 'education' in request.form:
                if request.form['education'] == 'yes':
                    answers['education']['yes'] += 1
                if request.form['education'] == 'no':
                    answers['education']['no'] += 1
                if request.form['education'] == 'mb':
                    answers['education']['mb'] += 1

            if 'queue' in request.form:
                if request.form['queue'] == 'yes':
                    answers['queue']['yes'] += 1
                if request.form['queue'] == 'no':
                    answers['queue']['no'] += 1
                if request.form['queue'] == 'mb':
                    answers['queue']['mb'] += 1

        if 'voted' in request.cookies and request.cookies['voted'] == 're':
            answers['sleep']['yes'] = 0
            answers['sleep']['no'] = 0
            answers['sleep']['mb'] = 0

            answers['education']['yes'] = 0
            answers['education']['no'] = 0
            answers['education']['mb'] = 0

            answers['queue']['yes'] = 0
            answers['queue']['no'] = 0
            answers['queue']['mb'] = 0

            if 'sleep' in request.form:
                if request.form['sleep'] == 'yes':
                    answers['sleep']['yes'] += 1
                if request.form['sleep'] == 'no':
                    answers['sleep']['no'] += 1
                if request.form['sleep'] == 'mb':
                    answers['sleep']['mb'] += 1

            if 'education' in request.form:
                if request.form['education'] == 'yes':
                    answers['education']['yes'] += 1
                if request.form['education'] == 'no':
                    answers['education']['no'] += 1
                if request.form['education'] == 'mb':
                    answers['education']['mb'] += 1

            if 'queue' in request.form:
                if request.form['queue'] == 'yes':
                    answers['queue']['yes'] += 1
                if request.form['queue'] == 'no':
                    answers['queue']['no'] += 1
                if request.form['queue'] == 'mb':
                    answers['queue']['mb'] += 1

            response = make_response(render_template('answers.html', answers=answers))
            response.set_cookie('voted', 'ok')
            return response


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4321)
