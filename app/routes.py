from flask import render_template

from app import app


@app.route('/index')
@app.route('/')
def index():
    my_value = 35
    my_string = 'Привет, всем!'
    my_true = True
    my_false = False
    my_list = [1, 2, 3, 4]

    context = {
        'my_value': my_value,
        'my_string': my_string,
        'my_true': my_true,
        'my_false': my_false,
        'my_list': my_list,
    }

    # Передаем словарь context в именованный аргумент context
    return render_template('index.html', context=context)
