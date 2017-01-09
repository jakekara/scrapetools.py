# scrapetools.py

Handles repetitive tasks associated with downloading all files linked on a
web page.

jake kara

jake@jakekara.com

January 2017

# Files

I often want to bulk download all of the links on a page, such as a web
page with a table of CSV or XLSX files. The scrapetools.py file has some
functions for handling some of the repetitive processes, including:

* creating directories to store output (if they don't exist)
* getting the web "index" page, which contains all the links
* downloading each link's href and saving it

In addition to scrapetools.py, there is an example of code I wrote using
scrapetools.py to scrape CT campaign finance data, called seec.py

# TODO

Sometimes you might want to name the files based on some other data on the
page, such as the text content of the link.
