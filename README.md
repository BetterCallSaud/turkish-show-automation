# Automating Streaming a Turkish show using Selenium

## Backstory
The story behind creating this automation script is very interesting. My grandpa was watching this Turkish TV show, *Payitaht Abdulhamid*, based on the last Caliph of the Ottoman Empire. There is a smart TV in our living room that could stream it on its Internet browser. But searching for the streaming website, choosing the episode and then playing it, was a tedious work. 

So we shifted to setting up an HDMI with a laptop onto the TV and then streaming the episodes on the laptop's web browser (Chrome in our case).

Now the interesting stuff!

Since no one else in the house is as technical as am I, I had to constantly go to the living room to change the episode once my grandpa had seen it. My focus and patience was disrupted bad and I started getting frustrated with my grandpa.

I knew I had to solve this problem and put out the fire in my brain!

**My idea:** *Automate the streaming so that I can relax! 9-10 hours of coding, debugging and testing; and I can just run the script in a few seconds and save 5-10 minutes per episode.*

## What I did?
I scoured the Internet for automation scripts and I came across **Selenium** in Python.

[Selenium Python](https://selenium-python.readthedocs.io/) bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver. Through Selenium Python API you can access all functionalities of Selenium WebDriver in an intuitive way.

I first searched for a URL, on which the show could be streamed directly. That is, if you open up that URL in the browser, it will show you a media player in the site and you can just play and watch the episode.

Once I did that, I used Selenium's automation API to create an automation script for this show. Here are the steps I followed: 

+ Downloaded Selenium's Chrome driver for Windows and configured it in the script
+ Charted out XML paths for various HTML elements on the streaming website, e.g. play button, mute button and fullscreen button
+ And then it's just a smart flow of the right clicks and interactions on the website

And then a few more hours of coding and caffeine...
And ta-da...

## Pre-Requisites
You should have `selenium` installed as a PyPI Package. To do this, run:

```pip install selenium```

To run the script, you need to give arguments as follows: `python abdulhamid.py <episode_number> <part_number>`.

Also, this script MAY NOT WORK, as it is the original version from 2 years ago. 

You can `open-source` the shit out of this if you want!
