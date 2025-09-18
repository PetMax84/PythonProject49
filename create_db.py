from app import db, app  # <-- импортируем app и db из пакета app

with app.app_context():
    db.create_all()
    print("Database created successfully!")