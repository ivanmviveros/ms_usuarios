- actualizar configuración de la BD en secrets.json
- aplicar migraciones a la BD, python manage.py migrate

docker build  . -t msusuarios
docker run -dit --cpus 1 --memory 1000MB --name msusuarios -p 8001:80 msusuarios

