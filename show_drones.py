import edgedb

# connect to the database
client = edgedb.create_client(dsn="hums_db")
results = []

# query the database
try:
    results = client.query("SELECT Drone {name, aircraft_id} ORDER BY .name")

except KeyError as ex:
    print(f"database query failed {str(ex)}")

# did we get any data?
if not results:
    print(f"database is empty")
else:
    print(f"results:\n{results}")
    print(f"\nDatabase has {len(results)} drone(s)")
    for result in results:
        print(f"Drone: {result.name} {result.aircraft_id}")

client.close()
print(f"Operation completed.")
