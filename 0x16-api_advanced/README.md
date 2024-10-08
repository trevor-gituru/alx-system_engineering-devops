#  0x16. API advanced

![api](/images/0_12_1.jpg)

## Background Context
Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

## Concepts learnt
- How to read API documentation to find the endpoints you’re looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Libraries imported in your Python files must be organized in alphabetical order
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use the Requests module for sending HTTP requests to the Reddit API

## Tasks
### 0. How many subs?
Write a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

**Hint:** No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

**Requirements:**

- Prototype: **def number_of_subscribers(subreddit)**
- If not a valid subreddit, return 0.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
```bash
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py programming
756024
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py this_is_a_fake_subreddit
0
```
### 1. Top Ten 
### 
### 
## Resources
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.wikipedia.org/wiki/Query_string)