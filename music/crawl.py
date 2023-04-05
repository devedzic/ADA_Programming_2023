"""Web scraping and crawling.
BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
"""
import pandas as pd
#%%
# Setup / Data
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from util import utility
from settings import *

#%%
# Getting started

# The Website to work with, i.e. to scrape info from and crawl over it - Ultimate Classic Rock.
# The starting URL refers to articles about George Harrison.
start_url = 'https://ultimateclassicrock.com/search/?s=George%20Harrison'

#%%
# Create Response object from GET request, using requests.get(<url>, allow_redirects=False)
response = requests.get(start_url, allow_redirects=False)
print(type(response))
print(response)

#%%
# Get response text from Response object, using <response>.text
response_text = response.text
print(response_text[:4000])

#%%
# Get BeautifulSoup object from response text, using BeautifulSoup(<response text>, 'html.parser')
soup = BeautifulSoup(response_text, 'html.parser')
# print(type(soup))
# print(soup)

#%%


def get_soup(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Creates Response object from HTTP GET request, using requests.get(<url string>, allow_redirects=False),
    and then uses the text field of the Response object and the 'html.parser' to create the BeautifulSoup object.
    """

    # Create Response object from HTTP GET request; assume that no redirection is allowed (allow_redirects=False)
    response = requests.get(url, allow_redirects=False)

    # Get text from the Response object, using <response>.text
    response_text = response.text

    # Create and return the corresponding BeautifulSoup object from the response text; use features='html.parser'
    return BeautifulSoup(response_text, features='html.parser')

#%%


# Test get_soup(url)
soup = get_soup(start_url)
# print(type(soup))
# print(str(soup))

#%%
# Save BeautifulSoup object to an HTML file,
# using <Path-file-object>.write_text(str(<BeautifulSoup object>), encoding='utf-8', errors='replace')
soup_file = DATA_DIR / 'soup.html'
soup_file.write_text(str(soup), encoding='utf-8', errors='replace')

#%%
# Demonstrate <BeautifulSoup object>.find('<tag>'); e.g., find the first 'span' tag.
span_first = soup.find('span')
print(span_first)
print()
print(type(span_first))

#%%
# Demonstrate <BeautifulSoup object>.find('<tag>').find('<nested tag>'); e.g., find the 'a' tag in an 'article' tag.
a_first = soup.find('article').find('a')
print(a_first)

#%%
# Demonstrate getting a tag with specific attributes
# using <BeautifulSoup object>.find('<tag>', {'<attribute>': '<value>'}); e.g., find the 'visually-hidden' tag.
visually_hidden = soup.find('span', {'class': 'visually-hidden'})
print(visually_hidden)
# article_date = div_content.findNext('div', {'class': 'auth-date'}).findNext('time')
# print(article_date)

#%%
# Demonstrate getting values of tag attributes,
# e.g. <BeautifulSoup object>.find('<tag>').text for an 'a' tag and for a 'visually-hidden' tag.
a_first = soup.find('article').find('a').text
print(a_first)
visually_hidden = soup.find('span', {'class': 'visually-hidden'}).text
print(visually_hidden)

#%%
# Demonstrate <BeautifulSoup object>.find_all(<tag>), e.g. for the 'article' tag; returns a ResultSet object.
articles = soup.findAll('article')
print(type(articles))
print(articles)
print()
for article in articles:
    print(article)
    print()
print()
print(len(articles))

#%%
# The following lines demonstrate that getting the soup with requests.get() does not capture all tags
# (those filled with JavaScript, e.g. 'time'). That's when using selenium.webdriver is better.
article_date = soup.find('div', {'class': 'auth-date'})
print(article_date)
article_date = soup.find('div', {'class': 'auth-date'}).findNext('time').text
print(article_date)
print(len(article_date))

#%%
# Selenium version, needed for extracting the <time> tag info
from selenium import webdriver
# Before running the following line, make sure to download and unzip chromedriver and put chromedriver.exe
# in the Scripts subfolder of your Python installation folder,
# e.g. C:\Users\Vladan\AppData\Local\Programs\Python\Python310\Scripts.
# To find the Python installation folder from a Python script or notebook, just run:
#   import sys
#   sys.executable
# The driver should be downloaded from https://chromedriver.chromium.org/downloads.
# Then you need not provide the path of the driver, just run: driver = webdriver.Chrome().
# (Adapted from https://stackoverflow.com/a/60062969/1899061.)
driver = webdriver.Chrome()

driver.get(start_url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup)

#%%
# Save BeautifulSoup object to an HTML file,
# using <Path-file-object>.write_text(str(<BeautifulSoup object>), encoding='utf-8', errors='replace')
soup_file = DATA_DIR / 'soup.html'
soup_file.write_text(str(soup), encoding='utf-8', errors='replace')
# driver.quit()

#%%


def get_soup_selenium(url: str) -> BeautifulSoup:
    """Returns BeautifulSoup object from the corresponding URL, passed as a string.
    Makes an HTTP GET request, using driver = webdriver.Chrome() from the selenium package and its driver.get(url).
    Then uses the page_source field of the driver object and the 'html.parser' to create and return the BeautifulSoup o.
    """

    driver = webdriver.Chrome()
    driver.get(url)
    return BeautifulSoup(driver.page_source, 'html.parser')

#%%


# Test get_soup_selenium(url)
soup = get_soup_selenium(start_url)
print(soup.find('article').find('div', {'class': 'content'}).find('a').text)
# a_first = soup.find('article').find('a').text
# print(a_first)
# print(type(soup))
# print(str(soup))

#%%
# Demonstrate occasional anomalies in the ResultSet returned by <BeautifulSoup object>.find_all(<tag>);
# note that they may be appearing only in the selenium version, not in the requests version

# The following lines show that there are 11 articles on the page, not 10.
# The 11th one is something else, not visible on the page at the first glance and should be eliminated from
# further processing.
articles = soup.findAll('article')
print(type(articles))
print(articles)
print()
for article in articles:
    print(article)
    print()

print(len(articles))

#%%
# The following line shows an anomaly in the articles ResultSet
print(articles[len(articles) - 1])

#%%
# Compare it to any of the other results from the Result set returned by ResultSet
# returned by <BeautifulSoup object>.find_all(<tag>).
print(articles[0])
print()
print(articles[len(articles) - 1])

#%%
# Demonstrate different ways of getting an attribute value for a tag (a bs4.element.Tag object),
# e.g. <tag>.find('<subtag>'), filtered with <{'class': "<class name>"}>;
# alternatively: <tag>.find('<tag>')['<attr>'], <tag>.find('<subtag>').get('<attribute>'),
# <tag>.find('<subtag>').<attribute>,... (<attribute>: e.g. text)
article = articles[0]
print(type(article))        # bs4.element.Tag
print()

print(article.find('a', {'class': 'theframe'}))
print(article.find('a')['class'])
print(article.find('a').get('class'))
print(article.find('a', {'class': 'theframe'}).text)

#%%
# Demonstrate <tag>.find_next_siblings() (returns all <tag>'s siblings) and
# <tag>.find_next_sibling() (returns just the first one)
all_articles_div = soup.find('div', {'class': 'rowline clearfix'})
# print(str(all_articles_div)[0:2000])
# print(all_articles_div.findAll)
# print(all_articles_div.find('span').findNext)
print(all_articles_div.find('span').find_next_sibling())
print()
siblings = all_articles_div.find('span').find_next_siblings()
for sibling in siblings:
    print(sibling, '\n')

#%%
# Each bs4.element.ResultSet, bs4.element.Tag,... can be used to create another BeautifulSoup object,
# using BeautifulSoup(str(<bs4.element object>), features='html.parser').
sibling_soup = BeautifulSoup(str(siblings[0]), 'html.parser')
print(type(sibling_soup))
print()
print(sibling_soup)

#%%
# Get/Return all text from a bs4.element.Tag object, using <bs4.element.Tag object>.text, e.g. for an 'article' tag.
print(sibling_soup.find('article').text)

#%%
# Get/Return and remove a specific item from a bs4.element.ResultSet using <result set>.pop(<index>) (default: last)
sibling = siblings.pop(1)
print(sibling)


#%%


def get_specific_page(start_url: str, page=1):
    """Returns a specific page from a Website where long lists of items are split in multiple pages.
    """

    if page > 1:
        return start_url.split('&searchpage=')[0] + '&searchpage=' + str(page)
    return start_url.split('&searchpage=')[0]


#%%
# Test get_specific_page(start_url, page)
print(get_specific_page(start_url + '&searchpage=1'))
print(get_specific_page(start_url + '&searchpage=1', 2))

#%%


def get_next_soup(start_url: str, page=1):
    """Returns the BeautifulSoup object corresponding to a specific page
    in case there are multiple pages that list objects of interest.
    Parameters:
    - start_url: the starting page/url of a multi-page list of objects
    - page: the page number of a specific page of a multi-page list of objects
    Essentially, get_next_soup() just returns get_soup(get_specific_page(start_url, page)),
    i.e. converts the result of the call to get_specific_page(start_url, page), which is a string,
    into a BeautifulSoup object.
    """

    return get_soup(get_specific_page(start_url, page))


#%%
# Test get_next_soup(start_url: str, page=1)
next_soup = get_next_soup(start_url, 2)
print(next_soup)

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

    return get_soup_selenium(get_specific_page(start_url, page))


#%%
# Test get_next_soup(start_url: str, page=1)
next_soup = get_next_soup_selenium(start_url, 2)
print(next_soup)


#%%
def crawl(url: str, max_pages=1):
    """Web crawler that collects info about specific articles from Ultimate Classic Rock,
    implemented as a Python generator that yields BeautifulSoup objects (get_next_soup() or get_next_soup_selenium())
    from multi-page movie lists.
    Parameters: the url of the starting page and the max number of pages to crawl in case of multi-page lists.
    """

    for page in range(max_pages):
        yield get_next_soup_selenium(url, page + 1)
        page += 1


#%%
# Test crawl(url: str, max_pages=1)
next_soup = crawl(start_url, 3)
while True:
    try:
        s = next(next_soup)
        for article in s.find_all('article')[:-1]:
            print(article.find('div', {'class': 'content'}).find('a').text)
            print()
    except StopIteration:
        break

#%%


def get_article_info_list(start_url: str, max_pages=1):
    """
    Returns structured information about articles related to Paul McCartney from a multi-page article list.
    :param start_url: the url of the starting page of a multi-page article list
    :param max_pages: the max number of pages to crawl
    :return: a list of tuples of info-items about the articles from a multi-page article list
    Creates and uses the following data:
    -
    """

    article_info_list = []
    next_soup = crawl(start_url, max_pages)
    while True:
        try:
            s = next(next_soup)
            for article in s.find_all('article')[:-1]:
                div_image = article.findNext('div', {'class': 'article-image-wrapper'})
                div_content = article.findNext('div', {'class': 'content'})
                featured_image_url = div_image.findNext('a').attrs['data-image']
                article_title = div_content.find('a').text
                article_date = div_content.find_next('time').text
                article_author = div_content.find_next('em').text.lstrip(' by  ')
                article_info_list.append((article_title, article_author, article_date, featured_image_url))
        except StopIteration:
            break
    return article_info_list

#%%


# Test get_articles_info(start_url: str, max_pages=1)
article_info_list = get_article_info_list(start_url, 3)
for article_info in article_info_list:
    print(article_info)

#%%
# Put everything in a csv file
csv_file = DATA_DIR / 'articles.csv'
df = pd.DataFrame(article_info_list, columns=['Title', 'Author', 'Date', 'Featured image'])
# df
df.to_csv(csv_file)

#%%
# Read back the csv file, just in case
df = pd.read_csv(csv_file)
display(df)


#%%
# Leftovers

# BASE_URL = 'https://www.imdb.com/'
# # Start from https://www.imdb.com, type anything in the Search box, and in the result find Advanced Search.
# # Click Keyword, and in Enter a keyword insert Paul McCartney. Select reference-to-paul-mccartney.

# Other candidates:
# https://ultimateclassicrock.com/search/?s=paul%20mccartney
# https://ultimateclassicrock.com/search/?s=albums
# https://www.rockarchive.com/artists?page=1
# https://digitaldreamdoor.com/pages/bg_hits/bg_hits_61.html
# https://www.paulmccartney.com/discography/albums/all
# https://rock-bands.com/
# https://rateyourmusic.com/charts/top/album/1960s/             # blocks IP address!

# Getting started
# start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key' \
#             '&sort=moviemeter,asc&mode=detail&page=1'
# start_url = 'https://www.imdb.com/search/keyword/?keywords=reference-to-paul-mccartney&ref_=kw_nxt&' \
#             'sort=moviemeter,asc&mode=detail&page=1'

# <BeautifulSoup object>.find_all(<tag>, {'<tag_attr_name>': "<tag_attr_value>"});
# use, e.g., 'h3' or 'div' as the tags in the examples (e.g., <div class="lister-item-image ribbonize">)
# h3_first = soup.find('h3')
# print(type(h3_first))
# print()
# print(h3_first)

# h3_first = soup.find('h3', {'class': "lister-item-header"})
# print(type(h3_first))
# print()
# print(h3_first)

# movie_items = soup.find_all('div', {'class': "lister-item mode-detail"})
# print(movie_items)
# print()

    # articles = soup.findAll('article')
    # print(type(articles))
    # # The following line shows that there are 11 articles on the page, not 10.
    # # The 11th one is something else, not visible on the page at the first glance and should be eliminated from
    # # further processing.
    # print(len(articles))
    # # # The following line shows an anomaly in the articles ResultSet.
    # # print(articles[len(articles) - 1])
    # # print()
    # for article in articles[:-1]:
    #     # image = article.findNext('a').find('figcaption').text
    #     # image = article.findNext('a').text
    #     # print(image)
    #     div_image = article.findNext('div', {'class': 'article-image-wrapper'})
    #     div_content = article.findNext('div', {'class': 'content'})
    #
    #     # # The following lines demonstrate that getting the soup with requests.get() does not capture all tags
    #     # # (those filled with JavaScript). That's why the solution with selenium.webdriver is better.
    #     # article_date = div_content.findNext('div', {'class': 'auth-date'}).findNext('time')
    #     # print(article_date)
    #
    #     featured_image_url = div_image.findNext('a').attrs['data-image']
    #     print(featured_image_url)
    #     article_title = div_content.find('a').text
    #     print(article_title)
    #     article_date = div_content.find_next('time').text
    #     print(article_date)
    #     article_author = div_content.find_next('em').text.lstrip(' by  ')
    #     print(article_author)


# if __name__ == "__main__":
#
#     articles = soup.findAll('article')
#     print(type(articles))
#     # The following line shows that there are 11 articles on the page, not 10.
#     # The 11th one is something else, not visible on the page at the first glance and should be eliminated from
#     # further processing.
#     print(len(articles))
#     # # The following line shows an anomaly in the articles ResultSet.
#     # print(articles[len(articles) - 1])
#     # print()
#     for article in articles[:-1]:
#         # image = article.findNext('a').find('figcaption').text
#         # image = article.findNext('a').text
#         # print(image)
#         div_image = article.findNext('div', {'class': 'article-image-wrapper'})
#         div_content = article.findNext('div', {'class': 'content'})
#
#         # # The following lines demonstrate that getting the soup with requests.get() does not capture all tags
#         # # (those filled with JavaScript). That's why the solution with selenium.webdriver is better.
#         # article_date = div_content.findNext('div', {'class': 'auth-date'}).findNext('time')
#         # print(article_date)
#
#         featured_image_url = div_image.findNext('a').attrs['data-image']
#         print(featured_image_url)
#         article_title = div_content.find('a').text
#         print(article_title)
#         article_date = div_content.find_next('time').text
#         print(article_date)
#         article_author = div_content.find_next('em').text.lstrip(' by  ')
#         print(article_author)
#
#
#     # Example: get all movie titles from an IMDb page
#     print()
#
#     # # Test get_soup()
#     # start_url = 'https://www.imdb.com/search/keyword/?keywords=rock-%27n%27-roll%2Crock-music&ref_=kw_ref_key&' \
#     #             'mode=detail&page=1&sort=moviemeter,asc'
#     print()
#
#     # Test get_specific_page()
#     print()
#
#     # Test get_next_soup()
#     print()
#
#     # Test crawl()
#     print()
#
#     # Test get_4_digit_substring()
#     print()
#
#     # Test get_m_info()
#     print()

