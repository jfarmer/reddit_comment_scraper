#!/usr/bin/env python

import sys
import argparse
import textwrap

try:
    import unicodecsv
    import praw
except ImportError:
    print '''\
You're missing some required packages.  Run the following command first:

    pip install -r requirements.txt
'''
    exit(1)

class RedditArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('Error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def main(argv):
    options = parse_arguments(argv)

    csv_filename = get_csv_filename(options.submission_id)

    client = authenticated_client(options.username, options.password)

    print('Fetching all comments for submission ' + options.submission_id + '.')
    print('If the submission has a lot of comments this could take a while.')
    print('When finished, the results will be saved to: ' + csv_filename)

    comments = get_all_submission_comments(client, options.submission_id)

    write_comment_csv(csv_filename, comments,
                      fieldnames=['id', 'link_id', 'parent_id', 'is_root',
                      'created_utc', 'author', 'gilded', 'downs', 'ups',
                      'score', 'is_root', 'author_flair_text', 'subreddit',
                      'subreddit_id', 'link_id', 'body'])

def parse_arguments(args):
    parser = RedditArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            '''
            A simple Python script to extract comments from a single Reddit
            thread and save them to a CSV file.

            Examples:
              python scrape_comments.py -u farmerje -p waffles123 2qmp46
              python scrape_comments.py -u username -p password submission_id
            '''
        )
    )

    parser.add_argument(
        '-u', '--username',
        dest='username',
        required=True,
        help='Your Reddit username')

    parser.add_argument(
        '-p', '--password',
        dest='password',
        required=True,
        help='Your Reddit password')

    parser.add_argument(
        'submission_id',
        type=str,
        help='A Reddit submission ID')

    return parser.parse_args(args)

def get_csv_filename(submission_id):
    return submission_id + '.csv'

def authenticated_client(username, password):
    client = praw.Reddit("Comment Scraper 1.0")
    client.login(username, password)
    return client

def get_all_submission_comments(client, submission_id):
    submission = client.get_submission(submission_id=submission_id)
    submission.replace_more_comments(limit=None, threshold=0)
    return praw.helpers.flatten_tree(submission.comments)

def filter_dict(dict, fields):
    return {k: v for k, v in dict.items() if k in fields}

def prepare_row(dict):
    return {k: v for k, v in dict.items()}

def write_comment_csv(filename, comments, fieldnames=[]):
    with open(filename, 'w') as csvfile:
        writer = unicodecsv.DictWriter(csvfile, fieldnames=fieldnames, encoding='utf-8')

        writer.writeheader()
        for comment in comments:
            row_data = filter_dict(comment.__dict__, fieldnames)
            writer.writerow(prepare_row(row_data))

if __name__ == "__main__":
    main(sys.argv[1:])
