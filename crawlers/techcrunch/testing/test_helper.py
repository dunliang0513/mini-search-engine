from crawlers.techcrunch import helper, crawler

# class TestHelper(object):
#     def test_extract_text_from_url(self):
#         url = 'https://techcrunch.com/2024/05/08/apples-crush-ad-is-disgusting/'
#         text = helper.extract_text_from_url(url)
#         print(text) 

import unittest
from unittest.mock import patch, MagicMock
from crawlers import common, techcrunch

class TestHelper(unittest.TestCase):
    @patch('crawlers.common.extract_urls_from_sitemap')
    @patch('crawlers.techcrunch.helper.extract_text_from_url')
    def test_crawl(self, mock_extract_text_from_url, mock_extract_urls_from_sitemap):
        # Arrange
        mock_extract_urls_from_sitemap.return_value = ['https://techcrunch.com/test-url-1/', 'https://techcrunch.com/test-url-2/']
        mock_extract_text_from_url.return_value = 'Test Text'
        visited_urls = set()

        # Act
        result = list(crawler.crawl(visited_urls))

        # Assert
        self.assertEqual(len(result), 2)
        self.assertIn(('https://techcrunch.com/test-url-1/', 'Test Text'), result)
        self.assertIn(('https://techcrunch.com/test-url-2/', 'Test Text'), result)

if __name__ == '__main__':
    unittest.main()