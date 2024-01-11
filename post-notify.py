import tweepy
from plyer import 

# Replace with your own Twitter API credentials
consumer_key = "consumer_key"
consumer_secret = "consumer_secret"
access_token = "access_token"
access_token_secret = "access_token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def notify_user(user, post):
    title = f"{user} has made a new post!"
    message = post.text
    .notify(
        title=title,
        message=message,
        app_name="Twitter Notifier",
        timeout=10,
    )

def main():
    user_to_monitor = "username_to_monitor"
    user_to_notify = "username_to_notify"

    try:
        user = api.get_user(user_to_monitor)
        for post in tweepy.Cursor(api.user_timeline, id=user_to_monitor).items():
            if post.user.screen_name == user_to_monitor:
                notify_user(user_to_monitor, post)
                break
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
