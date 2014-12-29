# Reddit Comment Scraper

This is a Reddit comment-scraping script written in Python.  To run it, you
will need to be able to run `python` from the command-line.  It will save the
results into a CSV file.  **Note**: it can take several minutes to run if
you ask it to scrape a submission with many comments.

If you don't have Python installed, the quickest way to get a working
installation is to use an online development environment like
[Cloud9](https://c9.io/).

## Installing and Running The Script

In this part, we assume you are able to open a command prompt and run
`python --version` without any problems.  If you don't know what those things
mean, don't know how to do them, or aren't able to do them, please read the
**[Requirements](#requirements)** section below.

To install the script, run the following from the command line:

```shell-session
pip install reddit_comment_scraper
```

You should now have a `scrape_comments` command available.  To see the various
ways to use the command run

```shell-session
scrape_comments --help
```

To scrape a given Reddit thread, run

```shell-session
scrape_comments -u reddit-username -p reddit-password submission_id
```

Here `reddit-username` and `reddit-password` are your _actual_ Reddit username
and password, respectively.  `submission_id` is the small, alphanumeric code
that Reddit uses to uniquely identify submissions.  For example, if the
submission whose comments you want to scrape has the following url

```text
http://www.reddit.com/r/pics/comments/2qj3v7
```

then the `submission_id` is `2qj3v7`.

## Requirements

This script is written using Python 2.7 and currently depends on two external
Python packages: `praw` and `unicodecsv`.  Before we install these packages, we
need to make sure you have Python 2.7 installed correctly.

If you're using a Mac, everything you need is already installed.  If you're
using Linux, we assume you know what you're doing.

### Installing Python on Windows

1.  **Download and Install Python 2.7**

    You can download the latest release of Python 2.7 from python.org, here:
    <https://www.python.org/downloads/windows/>.

    If you're using a 64-bit version of Windows, make sure to download the
    installer labeled **Windows x86-64 MSI Installer**.  If you're using a
    32-bit version of Windows, download the the installer labeled **Windows x86
    MSI Installer**. Note the missing **x86** in the name of the 32-bit
    installer.

    If you don't know whether you're running a 32-bit or 64-bit version of
    Windows, read _[Is my PC running the 32-bit or 64-bit version of Windows?](http://windows.microsoft.com/en-us/windows7/find-out-32-or-64-bit)_.

    **Sanity Check**: if everything installed correctly there should now be
    a `C:\Python27` directory on your computer.

2.  **Adding Python to Window's PATH Variable**

    We want to be able to run Python scripts by using the `python` command
    on the Windows command prompt.  By default, Windows doesn't know how to
    find the `python` command.  To fix this, navigate to

    ```text
    C:\Python27\Tools\Scripts
    ```

    You should see a list of files with strange names like `analyze_dep`,
    `checkpip`, `diff`, and so on.  These are individual Python scripts.

    Towards the bottom of the list you should see a script named `win_add2path`.
    Double-click that file to run it.  You will see a window appear briefly on
    screen and then disappear — this is normal!

3.  **Restart Your Computer**

    After you've installed Python 2.7 and run the `win_add2path` script, restart
    your computer.

4.  **Verifying Your Python Installation**

    We'll be running the script from the Windows Command Prompt.  If you don't
    know how to open a new command prompt read Microsoft's [Command Prompt:
    Frequently Asked Questions](http://windows.microsoft.com/en-us/windows/command-prompt-faq).

    After opening a new command prompt, run the following command:

    ```shell-session
    python --version
    ```

    If everything is installed correctly you should see the current version
    of Python printed out to the screen, e.g., `Python 2.7.9`.  If you see an
    error along the lines of

    ```text
    'python' is not recognized as an internal or external command
    ```

    then something is wrong with your Python installation.  Re-read the
    instructions above.
