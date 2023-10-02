import praw
reddit = praw.Reddit(client_id="", client_secret="", user_agent="")
subreddit = reddit.subreddit("Python")
for post in subreddit.hot(limit=5):
    print(post.title)
