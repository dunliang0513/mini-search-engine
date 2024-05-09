from crawlers import common
from crawlers.techcrunch import helper

def crawl(visited_urls):
    sitemap_url = 'https://techcrunch.com/site-map/'
    urls = common.extract_sitemaps(sitemap_url)
    for url in urls[:100]:
        if url not in visited_urls:
            visited_urls.add(url)
            text = helper.extract_text_from_url(url)
            yield url, text