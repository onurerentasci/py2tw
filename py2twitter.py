import tweepy
import keys_text as keys

client = tweepy.Client(
    keys.bearer_token,
    keys.api_key,
    keys.api_key_secret,
    keys.access_token,
    keys.access_token_secret,
)

auth = tweepy.OAuthHandler(
    keys.api_key, keys.api_key_secret, keys.access_token, keys.access_token_secret
)

api = tweepy.API(auth)


def tweet(message: str):
    updated_message = f"{message}"
    client.create_tweet(text=updated_message)
