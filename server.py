from flask import Flask, request, url_for,  render_template, json,redirect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    user = "Ученик Яндекс.Лицея"
    return render_template('base.html', title='title')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')