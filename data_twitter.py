import twitter
from utile.get_environment import get_configuration

config = get_configuration()
api = twitter.Api(
    consumer_key=config["consumer_key"],
    consumer_secret=config["consumer_secret"],
    access_token_key=config["access_token_key"],
    access_token_secret=config["access_token_secret"],
)

results = api.GetSearch(
    raw_query="q=twitter%20&result_type=recent&since=2014-07-19&count=100"
)

print(results)
