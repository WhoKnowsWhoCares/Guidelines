#!/bin/bash

set -a; source $1; set +a

#Lowercase BRANCH-name

CI_COMMIT_BRANCH=$( echo $CI_COMMIT_BRANCH | awk '{print tolower($0)}')

#Generate env-file

cat $1 | envsubst > env

#build App-container
/usr/bin/docker login -u gitlab-ci -p $CR_TOKEN registry.gitlab.com/repaname/backend
/usr/bin/docker build -t $CI_PROJECT_NAME-app-$BRANCH . -f Dockerfile
/usr/bin/docker tag $CI_PROJECT_NAME-app-$BRANCH registry.gitlab.com/repaname/backend/$CI_PROJECT_NAME-app-$BRANCH
/usr/bin/docker push registry.gitlab.com/repaname/backend/$CI_PROJECT_NAME-app-$BRANCH
