FROM postgis/postgis:15-master
COPY init.sql /docker-entrypoint-initdb.d/
RUN chmod -R 777 /var/lib/postgresql/data