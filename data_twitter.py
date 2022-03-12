import twitter
from utile.get_environment import get_configuration
from pprint import pprint
import tweepy
from datetime import datetime

config = get_configuration()


def twitter_api_connection(config):
    auth = tweepy.OAuth1UserHandler(
        consumer_key=config["consumer_key"],
        consumer_secret=config["consumer_secret"],
        access_token=config["access_token_key"],
        access_token_secret=config["access_token_secret"],
    )
    return auth


auth = twitter_api_connection(config)

api = tweepy.API(auth)


def get_company(
    company,
    lang=None,
    place=None,
    fromdate=200603210000,
    toDate=datetime.today().strftime("%Y%m%d%H%m"),
    maxResults=10,
):
    query = (
        f"({company} OR {company.title()} OR {company.lower()} OR {company.upper()})"
    )
    if lang:
        " ".join([query, f"lang:{lang}"])
    if place:
        " ".join([query, f"place:{place}"])

    output = api.search_full_archive(
        label="draft",
        query=f"({company} OR {company.title()} OR {company.lower()} OR {company.upper()}) lang:{lang} place:USA",
        fromDate=fromdate,
        toDate=toDate,
        maxResults=maxResults,
    )
    return output[0]


print(get_company("Criteo", "en", "USA")._json.keys())
