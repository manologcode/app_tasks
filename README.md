

al arrancar iniciar y correr migraciones

docker exec -it flask_tasks bash 

flask db init

flask db migrate -m "create tables"
flask db upgrade