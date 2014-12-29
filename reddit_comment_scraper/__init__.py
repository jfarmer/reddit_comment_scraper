import sys
import os
import argparse
import textwrap
import unicodecsv
import praw

if sys.platform == 'win32':
    import ctypes.wintypes


class RedditArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('Error: %s\n' % message)
        self.print_help()
        sys.exit(2)

def main():
    options = parse_arguments(sys.argv[1:])

    csv_file_path = get_csv_file_path(options.submission_id)

    client = authenticated_client(options.username, options.password)

    print(textwrap.dedent(
        '''\
        Fetching all comments for submission '{0}'. This could take a while...

        When finished, the results will be saved to:
          {1}\
        '''
    ).format(options.submission_id, csv_file_path))

    comments = get_all_submission_comments(client, options.submission_id)

    write_comment_csv(csv_file_path, comments,
                      fieldnames=['id', 'link_id', 'parent_id', 'is_root',
                      'created_utc', 'author', 'gilded', 'downs', 'ups',
                      'score', 'is_root', 'author_flair_text', 'subreddit',
                      'subreddit_id', 'link_id', 'body'])

def get_script_name():
    return os.path.basename(sys.argv[0])

def parse_arguments(args):
    parser = RedditArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            '''\
            A simple Python script to extract comments from a single Reddit
            thread and save them to a CSV file.

            Examples:
              {0} -u farmerje -p waffles123 2qmp46
              {0} -u username -p password submission_id\
            '''
        ).format(get_script_name())
    )

    parser.add_argument(
        '-u', '--username',
        dest='username',
        required=True,
        help='Your Reddit username'
    )

    parser.add_argument(
        '-p', '--password',
        dest='password',
        required=True,
        help='Your Reddit password'
    )

    parser.add_argument(
        'submission_id',
        type=str,
        help='A Reddit submission ID'
    )

    return parser.parse_args(args)

def authenticated_client(username, password):
    client = praw.Reddit('Comment Scraper 1.0')
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

def write_comment_csv(file_path, comments, fieldnames=[]):
    with open(file_path, 'w') as csvfile:
        writer = unicodecsv.DictWriter(
                    csvfile,
                    fieldnames=fieldnames,
                    encoding='utf-8'
                )

        writer.writeheader()
        for comment in comments:
            row_data = filter_dict(comment.__dict__, fieldnames)
            writer.writerow(prepare_row(row_data))

def get_csv_filename(submission_id):
    return "{0}.csv".format(submission_id)

def get_csv_file_path(submission_id):
    return file_data_path(get_csv_filename(submission_id))

def file_data_path(filename):
    return os.path.join(get_data_directory(), filename)

def get_data_directory():
    if sys.platform == 'win32':
        return get_windows_desktop_folder()
    elif sys.platform == 'darwin':
        return os.path.join(os.environ['HOME'], 'Desktop')
    else:
        return os.environ['HOME']

def get_windows_desktop_folder():
    CSIDL_DESKTOP = 0
    SHGFP_TYPE_CURRENT = 0

    buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
    ctypes.windll.shell32.SHGetFolderPathW(
        0, CSIDL_PERSONAL,
        0, SHGFP_TYPE_CURRENT,
        buf
    )

    return buf.value
