from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.models.guest import Guest
from server.models.episode import Episode
from flask import Blueprint, request, jsonify
from config import db

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    try:
        data = request.get_json()
        
        if not data or not all(k in data for k in ('rating', 'guest_id', 'episode_id')):
            return jsonify({'message': 'Rating, guest_id, and episode_id are required'}), 400
        
        # Validate guest and episode exist
        guest = Guest.query.get(data['guest_id'])
        episode = Episode.query.get(data['episode_id'])
        
        if not guest:
            return jsonify({'message': 'Guest not found'}), 404
        
        if not episode:
            return jsonify({'message': 'Episode not found'}), 404
        
        appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        
        db.session.add(appearance)
        db.session.commit()
        
        return jsonify(appearance.to_dict()), 201
    
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 400
