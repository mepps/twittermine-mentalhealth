Install pip 
(For Mac, either `sudo easy_install pip`, or `brew install pip`)

Install appropriate libraries

    pip install matplotlib --upgrade
    pip install pytz --upgrade
    pip install python-dateutil --upgrade
    pip install json
    pip install pandas


Create env.py with appropriate values

    import os

    os.environ["TWITTER_ACCESS_TOKEN"] =
    os.environ["TWITTER_ACCESS_TOKEN_SECRET"] =
    os.environ["CONSUMER_KEY"] = 
    os.environ["CONSUMER_SECRET"] =


Get Data from Twitter

    python twitter_streaming.py > twitter_mentalhealth.json

After enough tweets have been collected (running this script will tell you how many tweets there are)

    python twitter_mine.py
