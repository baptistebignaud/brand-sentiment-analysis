# brand-sentiment-analysis

https://forums.developer.nvidia.com/t/are-nvidia-docker-images-available-publicly/54619/6

bouding box of countries: https://data.humdata.org/dataset/bounding-boxes-for-countries/resource/aec5d77d-095a-4d42-8a13-5193ec18a6a9

countries continent: https://github.com/dbouquin/IS_608/blob/master/NanosatDB_munging/Countries-Continents.csv

Endpoints twitter API: https://developer.twitter.com/en/docs/twitter-api/migrate/twitter-api-endpoint-map

Filtering twitter API: https://developer.twitter.com/en/docs/twitter-api/premium/rules-and-filtering/premium-operators

Could be better to use country_profile but needs to have a paid premium account: https://developer.twitter.com/en/docs/tutorials/advanced-filtering-for-geo-data

Handle emojis

BERT finetuning: https://skimai.com/fine-tuning-bert-for-sentiment-analysis/

Profile users analysis: https://arxiv.org/pdf/1905.05961.pdf

# Usefull commands

## Build the container

`docker-compose build`

## Up containers

`docker-compose up -d`

## Stop containers

`docker-compose stop`

## Open a shell inside the main container

`docker-compose exec main_container sh`

## Run jupyter lab from the container

`jupyter lab --ip 0.0.0.0 --allow-root`
