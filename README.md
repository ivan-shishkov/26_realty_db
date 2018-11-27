# Real Estate Site

This is an example of a real estate agency site that allows you to display ads for real estate. 
Ads are stored in a SQLite database and can be loaded into it from JSON files. 
An example of such a JSON file is available [here](https://devman.org/fshare/1503424990/3/).

# Quickstart

For site launch on localhost need to install Python 3.5 and then install all dependencies:

```bash

$ pip install -r requirements.txt

```

To create database need to execute:

```bash

$ python3 db.py

```

To add ads to database from a JSON file need to execute:

```bash

$ python3 update_db.py --filepath /path/to/file_with_ads.json

```

Usage:

```bash

$ python3 server.py

```

Then open page [localhost:5000](http://localhost:5000) in browser.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
