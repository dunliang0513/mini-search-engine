import requests
from bs4 import BeautifulSoup

def extract_sitemaps(sitemap_url):
    response = requests.get(sitemap_url)
    if response.status_code != 200:
        return []
    
    soup = BeautifulSoup(response.text, 'xml')

    sitemap_tag = soup.find_all('sitemap')

    sitemaps = []

    for sitemap in sitemap_tag:
        website_loc = sitemap.find('loc').text
        sitemaps.append(website_loc)
    
    return sitemaps

def extract_urls(sitemap_url):
    response = requests.get(sitemap_url)
    if response.status_code != 200:
        return []
    
    soup = BeautifulSoup(response.text, 'xml')

    urls = []

    url_tags = soup.find_all('url')
    for url in url_tags:
        loc = url.find('loc').text
        urls.append(loc)

    return urls


            