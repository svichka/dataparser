## Usage

1. Bootstrap the DB
```bash
$ docker-compose up -d db
$ docker-compose run --rm flaskapp /bin/bash -c "cd /opt/services/flaskapp/src && python -c  'import database; database.init_db()'"
```

2. Bring up the cluster
```bash
$ docker-compose up -d
```

3. Launch bash in the container
```bash
$ docker exec -it nginx-flask-postgres-docker-compose-example_flaskapp_1 /bin/bash
```
browse to
```bash
$ /opt/services/flaskapp/src/saver
```

and run 

```bash
$ python global.py all
```
for separate running use following options:

`brand` - for parsing brands and families

`model` - for parsing car models fro the each family

`object` - for generate many-to-many table

`item` - for parsing items

## Troubleshooting

If you have a problems with modules etc, try to set env variable `$PYTHONPATH`:

```bash
$ export PYTHONPATH="/opt/services/flaskapp/src"
``` 