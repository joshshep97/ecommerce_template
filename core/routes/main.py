from flask import Blueprint, render_template

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/order-success/', methods=['GET'])
def order_success():
    return render_template(
        'stripe/success.html',
        title='Order Success'
    )

@main.route('/order-cancelled/', methods=['GET'])
def order_cancelled():
    return 'order cancelled'