from flask import Blueprint, jsonify, request
from heroes_service.extensions import db

heroes_bp = Blueprint("heroes_bp", __name__)

@heroes_bp.route("/")
def get_heroes():
    global db
    heroes = db.getHeroes()

    response = jsonify(heroes)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response