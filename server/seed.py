from app import app, db, User, Guest, Episode, Appearance
from datetime import date

def seed_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create users
        user1 = User(username='admin')
        user1.set_password('password123')
        
        user2 = User(username='testuser')
        user2.set_password('testpass')
        
        db.session.add_all([user1, user2])
        
        # Create guests
        guests = [
            Guest(name='Tom Hanks', occupation='Actor'),
            Guest(name='Oprah Winfrey', occupation='Media Mogul'),
            Guest(name='Elon Musk', occupation='Entrepreneur'),
            Guest(name='Taylor Swift', occupation='Musician'),
            Guest(name='Bill Gates', occupation='Philanthropist')
        ]
        
        db.session.add_all(guests)
        
        # Create episodes
        episodes = [
            Episode(date=date(2024, 1, 15), number=1),
            Episode(date=date(2024, 1, 22), number=2),
            Episode(date=date(2024, 1, 29), number=3),
            Episode(date=date(2024, 2, 5), number=4)
        ]
        
        db.session.add_all(episodes)
        db.session.commit()
        
        # Create appearances
        appearances = [
            Appearance(rating=5, guest_id=1, episode_id=1),
            Appearance(rating=4, guest_id=2, episode_id=1),
            Appearance(rating=3, guest_id=3, episode_id=2),
            Appearance(rating=5, guest_id=4, episode_id=3),
            Appearance(rating=4, guest_id=5, episode_id=4)
        ]
        
        db.session.add_all(appearances)
        db.session.commit()
        
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()