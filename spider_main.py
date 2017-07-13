# -*- coding: utf-8 -*-


import url_manager, html_downloader, html_parser, html_outputer

# 需创建以上四个模块

# http://baike.baidu.com/item/Python

# links = soup.find_all('a', href=re.compile(r"/item/(.*)"))

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()                # 初始化URL管理器
        self.downloader = html_downloader.HtmlDownloader()  # 初始化HTML下载器
        self.parser = html_parser.HtmlParser()              # 初始化HTML解析器
        self.outputer = html_outputer.HtmlOutputer()        # 初始化HTML输出器

    def crawl(self, root_url):
        count = 1       #爬取计数

        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print(("crawl %d: %s") % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count ==100:
                    break

                count = count +1
            except:
                print("crawl failed")
            

        self.outputer.output_html()


if __name__ =="__main__":
    root_url = "http://baike.baidu.com/item/Python"     # 入口URL
    obj_spider = SpiderMain()                           # 创建爬虫实例
    obj_spider.crawl(root_url)                          # 调用爬虫方法
