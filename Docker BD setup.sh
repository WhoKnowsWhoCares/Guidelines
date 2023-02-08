docker volume create prostgres_vol
docker volume create clickhouse_vol

docker network create db_net

# POSTGRES
docker run --rm -d \
	--name postgres_1 \
	-e POSTGRES_USER=alexander \
	-e POSTGRES_PASSWORD=Frants0241302 \
	-e POSTGRES_DB=db_pg \ 
	-v postgres_vol: /var/lib/postgresql/data \
	--net=db_net \
	postgres:14
	
# SUPERSET
docker run --rm -d -p 80:8080 --name superset apache/superset
docker exec -it superset superset fab create-admin \
	--username alexander \
	--firstname Alexander \
	--lastname Frantsev \
	--email as.frantsev@gmail.com \
	--password Frants0241302
	
docker exec -it superset superset db upgrade
docker exec -it superset superset init
