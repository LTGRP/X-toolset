import tweepy
from plyer import notification

# Replace with your own Twitter cookie file path
cookie_file_path = "/path/to/the/chookie.txt"

auth = tweepy.OAuthHandler("", "")
auth.set_cookie_file(cookie_file_path)

api = tweepy.API(auth)

def notify_user(user, post):
    title = f"{user} has made a new post!"
    message = post.text
    notification.notify(
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
