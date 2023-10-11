#!/bin/bash

set -a
source $1
set +a

if [[ $FLUSH == True ]]; then

    echo "WARNING! Run step Flush DB. Before wait 10 second's"
    sleep 10;
    docker exec app_$BRANCH python manage.py flush --noinput
    docker exec app_$BRANCH python manage.py migrate

else

if [[ $INIT == True ]]; then

echo "Run pipeline for Migrate DB and collectstatic"
/usr/bin/docker login -u gitlab-ci -p $CR_TOKEN registry.gitlab.com/repaname/backend
cat ci-config/docker-compose.yml.tmpl | envsubst > docker-compose.yml
cat $1 | envsubst > env
docker-compose -f docker-compose.yml pull 
docker-compose -f docker-compose.yml up -d --build --force-recreate
sleep 15
docker exec app_$BRANCH python manage.py makemigrations
docker exec app_$BRANCH python manage.py collectstatic --no-input --clear

    if [[ $CREATE_ADMIN == True ]]; then

        echo "Create Super User"
        docker exec app_$BRANCH python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.admin', '$ADMIN_PASS')"
    fi
else

echo "Run pipeline without Migrate and collectstatic"
/usr/bin/docker login -u gitlab-ci -p $CR_TOKEN registry.gitlab.com/repaname/backend
cat ci-config/docker-compose.yml.tmpl | envsubst > docker-compose.yml
cat $1 | envsubst > env
docker ps -q --filter name="app" | xargs -r docker stop
docker-compose -f docker-compose.yml pull 
docker container prune -f
docker-compose -f docker-compose.yml down -v
docker-compose -f docker-compose.yml up -d --build --force-recreate
sleep 5;
docker restart frontend-nginx-$BRANCH
sleep 10;
docker exec app_$BRANCH python manage.py migrate
docker exec app_$BRANCH python manage.py collectstatic --no-input --clear
fi

fi