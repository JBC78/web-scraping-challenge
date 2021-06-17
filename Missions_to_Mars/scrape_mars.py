#!/usr/bin/env python
# coding: utf-8

# In[1]:


# dependencies
import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ## NASA Mars News - Scrape the Mars News Site and collect the latest News Title and Paragraph Text

# In[3]:


# URL to be scraped
url = 'https://redplanetscience.com/'


# In[4]:


browser.visit(url)


# In[5]:


# Create a Beautiful Soup object with Splinter
html = browser.html
soup = bs(html, 'html.parser')


# In[6]:


print(soup)


# In[7]:


results = soup.select_one('div.list_text')


# In[8]:


print(results)


# In[9]:


news_title = soup.find('div', class_='content_title').get_text()


# In[10]:


print(news_title)


# In[11]:


news_body = soup.find('div', class_='article_teaser_body').get_text()


# In[12]:


print(news_body)


# ## JPL Mars Space Images - Featured Image

# In[13]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[14]:


# URL to be scraped
url = 'https://spaceimages-mars.com/'
browser.visit(url)


# In[15]:


# Use splinter to navigate the site and find the image url for the current Featured Mars Image
find_space_image = browser.find_by_tag('button')[1]
find_space_image.click()


# In[16]:


# Create a Beautiful Soup object with Splinter
html = browser.html
image_soup = bs(html, 'html.parser')


# In[17]:


# drill down to the full image url 
image_url = image_soup.find('img', class_='fancybox-image').get('src')


# In[18]:


image_url


# In[19]:


# assign the url string to a variable called featured_image_url


# In[20]:


featured_image_url = f'https://spaceimages-mars.com/{image_url}'
featured_image_url


# ## Mars Facts

# In[21]:


# Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet
# including Diameter, Mass, etc.
# Use Pandas to convert the data to a HTML table string.


# In[22]:


# create data frame
data_frame = pd.read_html('https://galaxyfacts-mars.com/')[0]
data_frame.head(50)


# In[23]:


# create table with Headers
data_frame.columns=['Description', 'Mars', 'Earth']
# set Description as index so the table looks similar to the web site facts
data_frame.set_index('Description', inplace=True)
data_frame


# In[24]:


# measure twice cut once
data_frame.to_html('table.html')
data_frame


# ## Mars Hemispheres

# In[31]:


# Visit the Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.
# You will need to click each of the links to the hemispheres in order to find the image url to the full
# resolution image.
# Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing 
# the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
# Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one 
# dictionary for each hemisphere.

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[32]:


# URL to be scraped
url = 'https://marshemispheres.com/'
browser.visit(url)


# In[33]:


# create a list to hold the high resolution images urls
high_res_hemisphere_images_urls = []


# In[34]:


hemisphere_links = browser.find_by_css('a.product-item img')
hemisphere_links


# In[35]:


for i in range(len(hemisphere_links)): 
    hemisphere = {} 
    browser.find_by_css('a.product-item img')[i].click()
    sample_element = browser.links.find_by_text('Sample').first
    hemisphere['img_url'] = sample_element['href']
    hemisphere['title'] = browser.find_by_css('h2.title').text
    high_res_hemisphere_images_urls.append(hemisphere)
    browser.back()


# In[36]:


hemisphere


# In[37]:


high_res_hemisphere_images_urls


# In[38]:


browser.quit()

