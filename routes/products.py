from flask import Blueprint, jsonify
from models.product import Product 

products_bp = Blueprint("Produtos", __name__)

@products_bp.get("")
def get():
    p = Product()
    return jsonify(p.get_all())
