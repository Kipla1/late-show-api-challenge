from flask import Blueprint, request, jsonify
from config import db
from server.models.guest import Guest
from flask_jwt_extended import jwt_required

guest_bp = Blueprint('guest_bp', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    try:
        guests = Guest.query.all()
        return jsonify([guest.to_dict() for guest in guests]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400
