#!/usr/bin/env bash
DUMP_NAME=db_dump_$(date +"%Y-%m-%dT%H-%M-%S")
docker-compose -f docker-compose.yml -f docker/docker-compose.prod.yml run --name $DUMP_NAME db \
        bash -c "pg_dump -h db -d happiness -U happiness -w > db_dump.sql" \
    && docker cp $DUMP_NAME:/db_dump.sql $DUMP_NAME.sql \
    && docker rm -f $DUMP_NAME \
    && tar -czf $DUMP_NAME.tar.gz $DUMP_NAME.sql \
    && rm $DUMP_NAME.sql \
    && gsutil cp $DUMP_NAME.tar.gz gs://happiness_backup/ \
    && rm $DUMP_NAME.tar.gz
