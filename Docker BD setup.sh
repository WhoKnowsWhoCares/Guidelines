docker volume create prostgres_vol
docker volume create clickhouse_vol

docker network create db_net

# POSTGRES
docker run --rm -d \
	--name postgres \
	-e POSTGRES_USER= \
	-e POSTGRES_PASSWORD= \
	-e POSTGRES_DB= \ 
	-v postgres_vol: /var/lib/postgresql/data \
	--net=db_net \
	postgres:14
	
# SUPERSET
docker run --rm -d -p 80:8080 --name superset apache/superset
docker exec -it superset superset fab create-admin \
	--username  \
	--firstname  \
	--lastname  \
	--email  \
	--password 
	
docker exec -it superset superset db upgrade
docker exec -it superset superset init
