import praw
import re

comment =\
"""
[HTML5 version, don't use giant!](http://%s)
"""

postedOn = []
r = praw.Reddit(user_agent='DM_Bot')
r.login('DailMail_Bot', 'password')
reddits = {} # Avoid these reddits

print "Logged in"
first = True

while True:
  try:
    submissions = r.get_domain_listing('giant.gfycat.com', sort='new',limit=100)
    for submission in submissions:
      if str(submission.subreddit).lower() not in reddits:

	if first == True:
	  postedOn.append(submission.id)

	if submission.id not in postedOn:
	  print "We got one! " + submission.short_link
	  subdomain = re.sub(r'^[^\.]*\.', "", submission.url);
	  link = re.sub(r'\.(gif|webm)$', "", subdomain);

	  try:
	    submission.add_comment(comment % (link))
	    print "Posted!"
	    postedOn.append(submission.id)
	  except:
	    print "Failed to submit."

    first = False
  except:
    print "Could not connect to reddit!"
