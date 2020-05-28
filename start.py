import time
from user_registry import app, database_initialization_sequence, db

if __name__ == '__main__':
    dbstatus = False
    while dbstatus == False:
        try:
            db.create_all()
        except:
            time.sleep(2)
        else:
            dbstatus = True
    database_initialization_sequence()
    app.run(host='0.0.0.0', port=80, debug=True)

