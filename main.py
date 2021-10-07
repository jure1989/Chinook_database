from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")

db.pretty_print("SELECT Name FROM Artist")

db.pretty_print("SELECT * FROM Invoice WHERE BillingCountry = 'Germany'")

number_of_albums = db.pretty_print("SELECT COUNT (*) FROM Album")

costumers_from_france = db.pretty_print("SELECT COUNT(*) FROM Customer WHERE Customer.Country = 'France'")

song_name = db.pretty_print("SELECT COUNT (*) FROM Track WHERE Track.Composer = 'AC/DC'")
