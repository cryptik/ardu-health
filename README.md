# HUMS DB for Web Weasels

https://www.edgedb.com/docs/reference/projects#ref-guide-using-projects

## Install the edgeDB driver
Using either the base environment or create a new conda (or other) environment for the project.

Install the edgedb driver as follows:

`pip install edgedb`

## Create the project database
Move into the project folder `ardu-health` and perform the following commands to setup and initialize the database.

`edgedb project init`

Use the database instance name `hums_db`

To remove the database exectue the following command `edgedb instance destroy -I hums_db --force`

To verify that edgedb is running `edgedb instance status -I hums_db`

To restart edgedb `edgedb instance restart -I hums_db`

## Update the DB Schema
To update the database schema, edit the `./dbschema/default.esdl` file with your changes and then create a migration to apply it to the database.

`edgedb migration create -I hums_db`
`edgedb migrate -I hums_db`

You can confirm the changes using with `edgedb list types -I hums_db`

Sometimes migrations can cause problem and not work as expectd.  When this happens, you can safely destroy the database with `edgedb instance destroy -I hums_db --force` and then follow the instructions to init the project again.



