# Reddit Comment Scraper

This is a Reddit comment-scraping script written in Python.  To run it, you
will need to be able to run `python` from the command-line.  It will save the
results into a CSV file.  **Note**: it can take several minutes to run if
you ask it to scrape a submission with many comments.

If you don't have Python installed, the quickest way to get a working
installation is to use an online development environment like
[Cloud9](https://c9.io/).

## Installing and Running The Script

First, download the script at
<https://github.com/jfarmer/reddit_comment_scraper/releases/latest>.

Next, install the required packages by running this while inside the
`reddit_comment_scraper` directory:

```shell-session
$ pip install -r requirements.txt
```

Finally, scrape some comments by running this while inside the
`reddit_comment_scraper` directory:

```shell-session
$ ./scrape_comments -u reddit-username -p reddit-password submission_id
```

Here `reddit-username` and `reddit-password` are your _actual_ Reddit username
and password, respectively.  `submission_id` is the small, alphanumeric code
that Reddit uses to uniquely identify submissions.  For example, if the
submission whose comments you want to scrape has the following url

```text
http://www.reddit.com/r/pics/comments/2qj3v7
```

then the `submission_id` is `2qj3v7`.
