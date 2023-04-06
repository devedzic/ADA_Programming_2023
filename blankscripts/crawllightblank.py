"""Web scraping and crawling.
BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""

#%%
# Setup / Data

# import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

from util import utility
from settings import *

#%%
# Getting started

# The Website to work with, i.e. to scrape info from and crawl over it - Ultimate Classic Rock.
# The starting URL refers to articles about George Harrison.
start_url = 'https://ultimateclassicrock.com/search/?s=George%20Harrison'


#%%
def get_soup_selenium(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Makes an HTTP GET request, using driver = webdriver.Chrome() from the selenium package and its driver.get(url).
    Then uses the page_source field of the driver object and the 'html.parser' to create and return the BeautifulSoup o.
    """

    # Before running the line driver = webdriver.Chrome(),
    # make sure to download and unzip chromedriver and put chromedriver.exe
    # in the Scripts subfolder of your Python installation folder,
    # e.g. C:\Users\Vladan\AppData\Local\Programs\Python\Python310\Scripts.
    # The driver should be downloaded from https://chromedriver.chromium.org/downloads.
    # Then you need not provide the path of the driver, just run: driver = webdriver.Chrome().
    # (Adapted from https://stackoverflow.com/a/60062969/1899061.)


#%%
# Test get_soup_selenium(url)


#%%
def get_specific_page(start_url: str, page=1):
    """Returns a specific page from a Website where long lists of items are split in multiple pages.
    """

#%%
# Test get_specific_page(start_url, page)


#%%
def get_next_soup_selenium(start_url: str, page=1):
    """Returns the BeautifulSoup object corresponding to a specific page
    in case there are multiple pages that list objects of interest, using selenium instead of requests.
    Parameters:
    - start_url: the starting page/url of a multi-page list of objects
    - page: the page number of a specific page of a multi-page list of objects
    Essentially, get_next_soup() just returns get_soup_selenium(get_specific_page(start_url, page)),
    i.e. converts the result of the call to get_specific_page(start_url, page), which is a string,
    into a BeautifulSoup object.
    """

#%%
# Test get_next_soup_selenium(start_url: str, page=1)


#%%
def crawl(url: str, max_pages=1):
    """Web crawler that collects info about specific articles from Ultimate Classic Rock,
    implemented as a Python generator that yields BeautifulSoup objects (get_next_soup() or get_next_soup_selenium())
    from multi-page movie lists.
    Parameters: the url of the starting page and the max number of pages to crawl in case of multi-page lists.
    """


#%%
# Test crawl(url: str, max_pages=1)

#%%
# Save BeautifulSoup object to an HTML file,
# using <Path-file-object>.write_text(str(<BeautifulSoup object>), encoding='utf-8', errors='replace').

#%%
# Demonstrate <BeautifulSoup object>.find('<tag>'); e.g., find the first 'article' tag.

#%%
# Demonstrate <BeautifulSoup object>.find('<tag>').find('<nested tag>'); e.g., find the 'a' tag in an 'article' tag.

#%%
# Demonstrate getting a dictionary of all attributes of a tag (e.g., for an 'a' tag nested in an 'article' tag),
# using <tag>.attrs.

#%%
# Demonstrate getting a tag with specific attributes
# using <BeautifulSoup object>.find('<tag>', {'<attribute>': '<value>'});
# e.g., find a 'div' tag with the 'article-image-wrapper' attribute, and then another 'div' tag with the 'content' att.

#%%
# Demonstrate getting values of tag attributes,
# e.g. <BeautifulSoup object>.find('<tag>').text for an 'a' tag and for a 'visually-hidden' tag.

#%%
# Demonstrate <BeautifulSoup object>.find_all(<tag>), e.g. for the 'article' tag; returns a ResultSet object.

#%%
# Demonstrate occasional anomalies in the ResultSet returned by <BeautifulSoup object>.find_all(<tag>);
# note that they may be appearing only in the selenium version, not in the requests version.

# The following lines show that there are 11 articles on the page, not 10.
# The 11th one is something else, not visible on the page at the first glance and should be eliminated from
# further processing.

#%%
# The following line shows an anomaly in the articles ResultSet.

#%%
# Compare it to any of the other results from the Result set returned by ResultSet
# returned by <BeautifulSoup object>.find_all(<tag>).

#%%
# Demonstrate <tag>.find_next_siblings() (returns all <tag>'s siblings) and
# <tag>.find_next_sibling() (returns just the first one); e.g., use the 'div' tag, class='rowline clearfix'.
# IMPORTANT: <tag> MUST be a Tag object (e.g., a 'span' tag) encompassed by ANOTHER tag (e.g., a 'div' tag) AND
# having same-level siblings (e.g., multiple 'span' tags at the same level), not a ResultSet object!!!

#%%
# Each bs4.element.ResultSet, bs4.element.Tag,... can be used to create another BeautifulSoup object,
# using BeautifulSoup(str(<bs4.element object>), features='html.parser').

#%%
# Get/Return all text from a bs4.element.Tag object, using <bs4.element.Tag object>.text, e.g. for an 'article' tag.

#%%
# Get/Return and remove a specific item from a bs4.element.ResultSet using <result set>.pop(<index>) (default: last).


#%%
def get_article_info_list(start_url: str, max_pages=1):
    """
    Returns structured information about articles related to George Harrison from a multi-page article list.
    :param start_url: the url of the starting page of a multi-page article list
    :param max_pages: the max number of pages to crawl
    :return: a list of tuples of info-items about the articles from a multi-page article list
    Creates and uses the following data:
    - article_title
    - article_date
    - article_author
    - featured_image_url
    """


#%%
# Test get_article_info_list(start_url: str, max_pages=1)

#%%
# Put everything in a csv file

# # Alternatuve 2, using Pandas
# csv_file = DATA_DIR / 'articles.csv'
# df = pd.DataFrame(article_info_list, columns=['Title', 'Author', 'Date', 'Featured image'])
# # df
# df.to_csv(csv_file)
