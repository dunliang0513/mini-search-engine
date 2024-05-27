from crawlers import common
from crawlers.techcrunch import helper

def crawl(visited_urls):
    
    sitemap_url = 'https://techcrunch.com/sitemap.xml'
    xml_list = common.extract_sitemap(sitemap_url)
    url_result = []
    
    # Can modify the range to get more urls
    for xml in xml_list[150:160]:
        url = common.extract_urls_from_xml(xml)
        url_result.append(url)

    # Flatten the url_result list from a nested list
    url_result = [item for sublist in url_result for item in sublist]

    for url in url_result[:50]:
      
        if url not in visited_urls:
            visited_urls.append(url)
            print(f"Visiting: {url}")
            # Extract the text from the url
            text = helper.extract_text_from_url(url)
    
            yield url, text

