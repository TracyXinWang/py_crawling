# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re 
from urllib import parse

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r"/item/"))
        for link in links:
            new_url = link['href']
            new_full_url = parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_ = "lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_ = "lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return 

        soup = BeautifulSoup(html_cont, 'html.parser')       # BeautifulSoup解析网页内容
        new_urls = self._get_new_urls(page_url, soup)       # 获取页面内容包含的URLs
        new_data = self._get_new_data(page_url, soup)       # 获取页面内容中想要爬取的数据
        return new_urls, new_data