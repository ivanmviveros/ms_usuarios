- actualizar configuración de la BD en secrets.json
- aplicar migraciones a la BD, python manage.py migrate

docker build  . -t msusuarios
docker run -dit --cpus 1 --memory 1000MB --name msusuarios -p 8001:80 msusuarios


ivanmvr@sth2fso2pc07:~/Escritorio$ ls -l docker*
-rwxrwxr-x 1 ivanmvr ivanmvr 675 nov 22  2018 docker-build-microservicios.sh
-rwxrwxr-x 1 ivanmvr ivanmvr 146 nov 24  2018 docker-build-monolitica.sh
-rwxrwxr-x 1 ivanmvr ivanmvr  99 nov 22  2018 docker-delete-microservicios.sh
-rwxrwxr-x 1 ivanmvr ivanmvr 477 feb  6  2019 docker-microservicios.sh
-rwxrwxr-x 1 ivanmvr ivanmvr 100 nov 24  2018 docker-monolitica.sh
-rwxrwxr-x 1 ivanmvr ivanmvr 153 nov 23  2018 docker-start-microservicios.sh
-rwxrwxr-x 1 ivanmvr ivanmvr 148 nov 22  2018 docker-stop-microservicios.sh
ivanmvr@sth2fso2pc07:~/Escritorio$ cat docker*
docker rm examenesappprincipal
docker rmi examenesappprincipal
docker rm examenesapi
docker rmi examenesapi
docker rm examenesmsusuarios
docker rmi examenesmsusuarios
docker rm examenesmsgrupos
docker rmi examenesmsgrupos
docker rm examenesmsexamenes
docker rmi examenesmsexamenes
docker build  ~/code/ExamenesAppPrincipal/examenesappprincipal/ -t examenesappprincipal
docker build  ~/code/ExamenesAPI/examenesapi/ -t examenesapi
docker build  ~/code/ExamenesMSUsuarios/examenesmsusuarios/ -t examenesmsusuarios
docker build  ~/code/ExamenesMSGrupos/examenesmsgrupos/ -t examenesmsgrupos
docker build  ~/code/ExamenesMSExamenes/examenesmsexamenes/ -t examenesmsexamenes





docker rm examenesmonolitico
docker rmi examenesmonolitico
docker build  ~/code/ExamenesMonolitico/examenesmonolitico/ -t examenesmonolitico





docker rm examenesmsusuarios examenesmsgrupos examenesmsexamenes examenesapi examenesappprincipal

docker run -dit --cpus 1 --memory 1000MB --name examenesmsusuarios -p 8001:80 examenesmsusuarios
docker run -dit --cpus 1 --memory 1000MB  --name examenesapi -p 8002:80 examenesapi
docker run -dit --cpus 0.5 --memory 700MB --name examenesmsgrupos -p 8003:80 examenesmsgrupos
docker run -dit --cpus 0.5 --memory 700MB --name examenesmsexamenes -p 8004:80 examenesmsexamenes
docker run -dit --cpus 1 --memory 1000MB --name examenesappprincipal -p 8008:80 examenesappprincipal



docker run -dit --cpus 3 --memory 3000MB --name examenesmonolitico -p 8080:80 examenesmonolitico



docker start examenesmsusuarios
docker start examenesapi
docker start examenesmsgrupos
docker start examenesmsexamenes
docker start examenesappprincipal
docker stop examenesmsusuarios
docker stop examenesapi
docker stop examenesmsgrupos
docker stop examenesmsexamenes
docker stop examenesappprincipal