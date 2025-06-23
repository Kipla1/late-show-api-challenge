from flask import Blueprint, request, jsonify
from config import db
from server.models.episode import Episode
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    try:
        episodes = Episode.query.all()
        return jsonify([episode.to_dict() for episode in episodes]), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    try:
        episode = Episode.query.get(id)
        if not episode:
            return jsonify({'message': 'Episode not found'}), 404
        
        return jsonify(episode.to_dict()), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    try:
        episode = Episode.query.get(id)
        if not episode:
            return jsonify({'message': 'Episode not found'}), 404
        
        db.session.delete(episode)
        db.session.commit()
        
        return jsonify({'message': 'Episode deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400
