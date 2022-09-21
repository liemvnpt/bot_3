FROM rasa/rasa:latest

COPY app /app
COPY server.sh /app/server.sh

USER root
RUN chmod -R 777 /app
USER 1001

RUN rasa train nlu
CMD $(echo “rasa run -p $PORT -m models --credentials credentials.yml --enable-api --log-file out.log --endpoints endpoints.yml” | sed ‘s/=//’)

ENTRYPOINT ["/app/server.sh"]