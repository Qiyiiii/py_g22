# execute ./script.sh
sqlite3 matchapp.db < schema.sql
# sqlite3 matchapp.db < data.sql
sqlite3 matchapp.db < InsertUserUS.sql
sqlite3 matchapp.db < InsertInterests.sql
sqlite3 matchapp.db <InsertActions.sql
python3 matchapp/app/app.py