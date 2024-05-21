import requests
from bs4 import BeautifulSoup


def extract_text_from_url(url):
    try:
        res = requests.get(url)
        # Raises an HTTPError for bad responses
        res.raise_for_status()  

    except requests.RequestException as e:
        print(f"Request error: {e}")
        return ''
    
    try:
        soup = BeautifulSoup(res.text, 'html.parser')
        
        h1 = soup.find('h1', class_='wp-block-post-title')
        h2 = soup.find('p', id='speakable-summary')
        main_content = soup.find('div', class_='wp-block-post-content')
        
        if h1 is None or h2 is None or main_content is None:
          print("Required elements not found in the HTML.")
          return ''
        
        main_paragraphs = main_content.find_all('p')

        # Filter out paragraphs that are ads
        filtered_paragraphs = [p.get_text().strip() 
                               for p in main_paragraphs 
                               if not p.find_parent(class_='ad-unit wp-block-tc-ads-ad-slot')]
        
        chunks = [h1.get_text().strip()
        , *filtered_paragraphs]

        return '\n'.join(chunks)
    
    except Exception as e:
        print(f"Parsing error: {e}")
        return ''