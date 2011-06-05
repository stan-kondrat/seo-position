#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import httplib
import urllib2
import cookielib
import lxml.html

class check():
    def __init__(self, query, url):
        """docstring for __init__"""
        self.query = query
        self.url = url

    def google(self):
        request = urllib2.Request((u'http://www.google.com/search?as_q=%s&as_epq=&as_oq=&as_eq=&hl=ru&client=ubuntu&tbo=1&channel=fs&num=100&lr=&cr=&as_ft=i&as_filetype=&as_qdr=all&as_occt=any&as_dt=i&as_sitesearch=&as_rights=&safe=images&btnG=Поиск+в+Google' % self.query).encode('utf8'))
        #Create a CookieJar object to hold the cookies
        cj = cookielib.CookieJar()
        #Create an opener to open pages using the http protocol and to process cookies.
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.HTTPHandler())
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11')
        doc = lxml.html.document_fromstring(opener.open(request).read())
        for i, result in enumerate(doc.cssselect('h3 a')):
            if self.url in result.get('href'):
                print 'Google - ', i

    def yandex(self):
        """docstring for yandex"""
        request = urllib2.Request((u'http://yandex.ru/yandsearch?text=%s&numdoc=50&lr=66' % self.query).encode('utf8'))
        #Create a CookieJar object to hold the cookies
        cj = cookielib.CookieJar()
        #Create an opener to open pages using the http protocol and to process cookies.
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj), urllib2.HTTPHandler())
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11')
        doc = lxml.html.document_fromstring(opener.open(request).read())
        for i, result in enumerate(doc.cssselect('h2 a')):
            if self.url in result.get('href'):
                print 'Yandex - ', i


if __name__ == "__main__":
    seo_position = check(query=sys.argv[1], url=sys.argv[2])
    seo_position.google()
    seo_position.yandex()
