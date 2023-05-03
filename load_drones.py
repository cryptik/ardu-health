import edgedb

data = [["Boba", "FM345RF8734", "Boba"],
            ["Mando", "FM345RF8734", "Mando"],
            ["Bo Katan", "FM345RF8734", "Bo Katan"]]

# connect to the database
client = edgedb.create_client(dsn="hums_db")

# delete the table data
try:
    client.query("""delete Drone""")
except KeyError as ex:
    print(f"database delete failed {str(ex)}")

# insert the data
for row in data:
    try:
        client.query("""
            insert Drone {
                name := <str>$name,
                aircraft_id := <str>$aircraft_id,
                callsign := <str>$callsign,
            }
            """, name=row[0], aircraft_id=row[1], callsign=row[2])
    except KeyError as ex:
        print(f"database load failed {str(ex)}")

client.close()
print(f"Operation completed.")
