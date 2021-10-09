from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("Chinook_Sqlite.sqlite")

db.pretty_print("SELECT Name FROM Artist")

db.pretty_print("SELECT * FROM Invoice WHERE BillingCountry = 'Germany'")

number_of_albums = db.pretty_print("SELECT COUNT (*) FROM Album")

costumers_from_france = db.pretty_print("SELECT COUNT(*) FROM Customer WHERE Customer.Country = 'France'")

song_name = db.pretty_print("SELECT COUNT (*) FROM Track WHERE Track.Composer = 'AC/DC'")

# What order (Invoice) was the most expensive? Which one was the cheapest?
min_order = db.pretty_print("SELECT MIN (Total) AS Smallest FROM Invoice")

max_order = db.pretty_print("SELECT MAX (Total) AS MostExpansive FROM Invoice")

# Which city (BillingCity) has the most orders?
db.pretty_print('SELECT BillingCity, COUNT(InvoiceId) AS MostOrders FROM Invoice GROUP BY BillingCity ORDER BY '
                'MostOrders DESC')

# Calculate (or count) how many tracks have this MediaType: Protected AAC audio file
media_type = db.pretty_print("""SELECT COUNT (*) FROM Track
                             JOIN MediaType ON MediaType.MediaTypeId = Track.MediaTypeId
                             WHERE MediaType.Name = 'Protected AAC audio file'""")

# Find out what Artist has the most albums?
most_albums = db.pretty_print("""SELECT Artist.Name, COUNT(*) AS MostAlbums
                              FROM Artist
                              JOIN Album ON Album.ArtistId = Artist.ArtistId
                              GROUP BY Album.ArtistId
                              ORDER BY MostAlbums DESC
                              """)

# What genre has the most tracks?
most_tracks = db.pretty_print("""SELECT Genre.Name, COUNT(*) AS MostTracks
                              FROM Genre
                              JOIN Track ON Track.GenreId = Genre.GenreId
                              GROUP BY Track.GenreId
                              ORDER BY MostTracks DESC
                              """)

# Which customer spent the most money so far?
most_money = db.pretty_print("""SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS MostMoney
                             FROM Customer
                             JOIN Invoice ON Invoice.CustomerId = Customer.CustomerId
                             GROUP BY Invoice.CustomerId
                             ORDER BY MostMoney DESC
                             """)

# What songs were bought with each order?
bought_songs = db.pretty_print("""SELECT Invoice.InvoiceId, Track.Name
                               FROM Invoice
                               JOIN InvoiceLine ON InvoiceLine.InvoiceId = Invoice.InvoiceId
                               JOIN Track ON InvoiceLine.TrackId = Track.TrackId
                               """)
