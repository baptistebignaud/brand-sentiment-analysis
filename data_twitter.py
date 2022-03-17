import twitter
from utile.get_environment import get_configuration
from pprint import pprint
import tweepy
from datetime import datetime
import pandas as pd
import snscrape.modules.twitter as sntwitter
from fuzzymatcher import link_table, fuzzy_left_join
import json
from geopy import distance
import numpy as np


# Get geographical informations
countries_bounding_boxes = pd.read_csv("./material/country-boundingboxes.csv")

# Correct some mispellings
df_countries = pd.read_csv("./material/Countries-Continents.csv")
df_countries.loc[df_countries["Country"] == "US", "Country"] = "United States"
df_countries.loc[df_countries["Country"] == "CZ", "Country"] = "Czech Republique"
df_countries.loc[df_countries["Country"] == "Russian Federation", "Country"] = "Russia"

countries_bounding_boxes.loc[
    countries_bounding_boxes["country"] == "Czech Republ", "country"
] = "Czech Republique"
countries_bounding_boxes.loc[
    countries_bounding_boxes["country"] == "Liechtenstei", "country"
] = "Liechtenstein"

# Fuzzy match to match name of countries/continent and bounding boxes
left_on = "Country"
right_on = "country"
dfleft = df_countries
dfright = countries_bounding_boxes
countries_file = fuzzy_left_join(dfleft, dfright, left_on, right_on)
# exit(1)
countries_file = countries_file[
    ["Continent", "Country", "longmin", "latmin", "longmax", "latmax"]
]

# Get tweets about a company (with a scrapper)
# For the localization of the countries we used the circumscribed circle with center the center of the bouding box of the country and as radius the distance from the center to one extremity (we also added a small margin)
# Some more accurate techniques could be used (such as circumscribed circle of the polygon of the country or filter by location with twitter API)


def get_company(
    company: str,
    lang: str = None,
    place: str = None,
    fromdate: str = None,
    toDate: str = None,
) -> pd.DataFrame:
    """
    Function to get tweets with the name of the company as keyword and some possible filters
    company: param: Name of the company
    lang: param: Language of the tweet
    place: param: Country of the geolocalised tweet
    fromdate: param: From when you want the tweets
    toDate: param: Until when you want the tweets
    returns: Tweets with the company of keyword and some filters
    """
    df = pd.DataFrame([])
    query = f"{company} OR {company.title()} OR {company.lower()} OR {company.upper()}"
    if place:
        # Get coordinates of the country
        row = countries_file[countries_file["Country"] == place]
        longmin, latmin, longmax, latmax = row[
            ["longmin", "latmin", "longmax", "latmax"]
        ].iloc[0]
        longmean = (longmin + longmax) / 2
        latmean = (latmin + latmax) / 2
        middle = (latmean, longmean)
        ext = (latmin, longmin)
        dist = distance.distance(middle, ext).miles
        query = " ".join(
            [
                query,
                f"geocode:{latmean},{longmean},{min(float(700),float(dist+300))}mi",
            ]
        )

    if lang:
        query = " ".join([query, f"lang:{lang}"])
    if fromdate:
        query = query = " ".join([query, f"until:{fromdate}"])
    if toDate:
        query = query = " ".join([query, f"until:{toDate}"])

    # Iterate through scrapper to get tweets
    for _, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        d = json.loads(tweet.json())
        results = pd.json_normalize(d)

        # print(results)
        if not results.empty:
            results["country"] = place
            try:
                df = pd.concat([df, results])
            except:
                df = results
        if len(df) >= 1000:
            break
    return df


results = get_company(company="Sephora", lang="en", place="United States")


def get_all_countries(company) -> pd.DataFrame:
    """
    Function to get tweets with the name of the company as keyword for all countries in Europe Asia and North America
    company: param: Name of the company
    returns: Tweets with the company
    """
    # Go through all countries in Europe and Asia and North America for Sephora
    df = pd.DataFrame([])
    df_countries = pd.read_csv("./material/Countries-Continents.csv")
    # print(df.columns)
    list_countries_europe = countries_file[countries_file["Continent"] == "Europe"][
        "Country"
    ].unique()
    for country in list_countries_europe:
        print(country)
        results = get_company(company, "en", place=country)
        df_results = pd.DataFrame(results)

        if not df_results.empty:
            if df.empty:
                df = df_results
            else:
                df = pd.concat([df, df_results])

    list_countries_north_america = countries_file[
        countries_file["Continent"] == "North America"
    ]["Country"].unique()
    for country in list_countries_north_america:
        print(country)
        results = get_company(company, "en", place=country)
        df_results = pd.DataFrame(results)
        if not df_results.empty:
            df = pd.concat([df, df_results])

    list_countries_asia = countries_file[countries_file["Continent"] == "Asia"][
        "Country"
    ].unique()
    for country in list_countries_asia:
        print(country)
        results = get_company(company, "en", place=country)
        df_results = pd.DataFrame(results)
        if not df_results.empty:
            df = pd.concat([df, df_results])

    return df
df = get_all_countries("sephora")
df.to_csv("./data/all_countries.csv")


## If you want to use the api
# config = get_configuration()

# def twitter_api_connection(config):
#     auth = tweepy.OAuth1UserHandler(
#         consumer_key=config["consumer_key"],
#         consumer_secret=config["consumer_secret"],
#         access_token=config["access_token_key"],
#         access_token_secret=config["access_token_secret"],
#     )
#     return auth


# auth = twitter_api_connection(config)

# api = tweepy.API(auth)


# def get_company(
#     company,
#     lang=None,
#     place="USA",
#     fromdate=202203121418,
#     toDate=datetime.today().strftime("%Y%m%d%H%m"),
#     maxResults=100,
# ):
#     # print(tweepy.__version__)
#     # for page in tweepy.Cursor(
#     #     api.search_30_day,
#     #     # environment_name="draft",
#     #     label="development",
#     #     query=f"({company} OR {company.title()} OR {company.lower()} OR {company.upper()}) lang:{lang} place:USA",
#     #     # fromDate=fromdate,
#     #     # toDate=toDate,
#     #     maxResults=10,
#     # ).items(2):

#     # print("ok")
#     # print(page)
#     # return page
#     query = (
#         f"({company} OR {company.title()} OR {company.lower()} OR {company.upper()})"
#     )
#     if lang:
#         " ".join([query, f"lang:{lang}"])
#     if place:
#         " ".join([query, f"place:{place}"])

#     output = api.search_30_day(
#         label="development",
#         query=f"({company}  OR {company.lower()} OR {company.upper()}) lang:{lang} place:{place}",
#         maxResults=maxResults,
#     )
#     return output
