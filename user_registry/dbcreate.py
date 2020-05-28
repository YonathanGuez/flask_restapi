from user_registry import db, users
db.create_all()
test_rec = users(
        'Marco Hemken',
        'Los Angeles',
        '123 Foobar Ave',
        '12345'
        )
db.session.add(test_rec)
db.session.commit()