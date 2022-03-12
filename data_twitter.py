import twitter
from utile.get_environment import get_configuration
from pprint import pprint

config = get_configuration()
# print(config)
api = twitter.Api(
    consumer_key=config["consumer_key"],
    consumer_secret=config["consumer_secret"],
    access_token_key=config["access_token_key"],
    access_token_secret=config["access_token_secret"],
)


def get_company(company):
    results = api.GetSearch(
        raw_query=f"q={company}%20&result_type=recent&since=2014-07-19&count=2&lang=en"
    )
    return results


results = get_company("Criteo")
print(results[0])
print("\n", results[0]._json.keys())
