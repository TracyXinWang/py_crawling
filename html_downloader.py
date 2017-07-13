# -*- coding: utf-8 -*-

from urllib import request

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        #打开网页
        response = request.urlopen(url)

        if response.getcode()!=200:
            return None

        return response.read().decode("utf-8")
    