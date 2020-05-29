- actualizar configuración de la BD en secrets.json y en _datos_iniciales/secrets_inicial.json
- agregar acceso desde la ip del host a la BD. Modificar el archivo pg_hba.conf.
Agregar la siguiente linea al final del archivo actualizando la ip del equipo host:  
host    all             all             192.168.0.2/32            md5

- aplicar migraciones a la BD, python manage.py migrate


docker build  . -t msusuarios
docker run -dit --cpus 1 --memory 1000MB --name msusuarios -p 8001:80 msusuarios

