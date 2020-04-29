from flask import Blueprint, render_template
from storage import PRODUCTS


products_app = Blueprint('products_app', __name__)


@products_app.route('/', endpoint='products')
def products_page():
    products = PRODUCTS
    response = render_template(
        'product_list.html',
        product_list=products,
    )
    return response


@products_app.route('/<int:product_id>/', endpoint='product')
def product_page(product_id):
    products = PRODUCTS
    response = render_template(
        'product.html',
        product=products[product_id-1],
    )
    return response
