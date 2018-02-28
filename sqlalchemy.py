from sqlalchemy import create_engine
engine = create_engine('postgresql://satyam:123456789@localhost/satyam')
connection = engine.connect()
result = connection.execute("select name from company")
for row in result:
    print "username:", row['name']
connection.close()
