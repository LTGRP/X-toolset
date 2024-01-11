import tweepy
from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_user_followers(screen_name):
    followers = []
    for follower in tweepy.Cursor(api.followers, screen_name=screen_name, count=200).items():
        followers.append(follower.screen_name)
    return followers

def get_user_posts(screen_name):
    posts = api.user_timeline(screen_name=screen_name, count=1, include_rts=False, tweet_mode="extended")
    return posts[0].full_text.count(" ") + 1

def main():
    screen_name = input("Enter the username: ")
    followers = get_user_followers(screen_name)
    print(f"The followers of {screen_name}:")
    for follower in followers:
        post_count = get_user_posts(follower)
        print(f"{follower}: {post_count} posts")

if __name__ == "__main__":
    main()
