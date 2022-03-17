# Brand-sentiment-analysis

The aim of this project is to help Criteo to offer a brand analysis service to its clients during the 2024 Paris Olympic Games(to choose the right audiences to target target the users at the right time, to collect even more insights about partners brand & products). It is a draft of a solution. The aim of this repository is to first gather ideas that could be explored.
<br><br>

# The ideas for the solution

The main idea is to collect data from social media and to analyze the audience through different factors, and see how they react to a given brand. Our main focus was on Twitter because it was quite straightforwad to get the data but the analysis could be extended to other social media such as Instagram, Facebook or Reddit.<br>
Firstly, we developped a model (BERT) that given a tweet could understand if the person who was writting the tweet about the company was more postivie or negative. Then for each user that tweeted, we tried to get solutions to analyze their profile (we identify some models and solutions which could be used to determine key factors for people;e.g: age/gender/is a real person and also the personnality traits). Due to the lack of time of the project, we couldn't spend too much time to try to implement all models and construct the whole pipeline. <br>We integrated the guess of age and gender in our analysis but not the rest.

# Relevant references and links for our study

docker image with pytorch: https://forums.developer.nvidia.com/t/are-nvidia-docker-images-available-publicly/54619/6

bert model: https://en.wikipedia.org/wiki/BERT_(language_model)

bouding box of countries: https://data.humdata.org/dataset/bounding-boxes-for-countries/resource/aec5d77d-095a-4d42-8a13-5193ec18a6a9

countries continent: https://github.com/dbouquin/IS_608/blob/master/NanosatDB_munging/Countries-Continents.csv

Endpoints twitter API: https://developer.twitter.com/en/docs/twitter-api/migrate/twitter-api-endpoint-map

Filtering twitter API: https://developer.twitter.com/en/docs/twitter-api/premium/rules-and-filtering/premium-operators

Some premium filtering for twitter api: https://developer.twitter.com/en/docs/tutorials/advanced-filtering-for-geo-data

BERT finetuning: https://skimai.com/fine-tuning-bert-for-sentiment-analysis/

Profile users analysis: https://arxiv.org/pdf/1905.05961.pdf

Five big traits : https://github.com/jkwieser/personality-detection-text

For facebook big5 traits: https://github.com/jcl132/personality-prediction-from-text

Text based personality prediction from multiple social media data sources using pre-trained language model and model averaging:
https://journalofbigdata.springeropen.com/articles/10.1186/s40537-021-00459-1#availability-of-data-and-materials

Prediction of age and gender: https://github.com/euagendas/m3inference

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
