#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

import os
import sys
import time
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse, urldefrag
from urllib.error import HTTPError
from html.parser import HTMLParser
from queue import Queue, Empty
from threading import Thread, Lock
from datetime import datetime

ignore_403_errors = True
ignore_http_usage = True
ignore_blog_errors = True
ignore_shop_502_errors = True

errors = Queue()

pending_urls = Queue()
pending_urls.put((None, 'https://www.tinkerforge.com/'))

seen_urls = set()
seen_urls_lock = Lock()

def report_error(index, kind, base_url, url, e):
    if ignore_403_errors and isinstance(e, HTTPError) and e.code == 403:
        pass
    elif ignore_shop_502_errors and isinstance(e, HTTPError) and e.code == 502 and 'www.tinkerforge.com/' in url and '/shop/' in url:
        pass
    else:
        errors.put((base_url, url, repr(e)))
        print(index, 'error', kind, base_url, '->', url, e)

class Parser(HTMLParser):
    def __init__(self, index, base_url):
        super().__init__()

        self.index = index
        self.base_url = base_url

    def check_url(self, kind, url):
        print(self.index, kind, self.base_url, '->', url, '...')

        retries = 3

        while True:
            try:
                with urlopen(url) as r:
                    data = r.read(1)

                break
            except Exception as e:
                retries -= 1

                if retries >= 0:
                    time.sleep(5)
                    continue

                report_error(self.index, kind, self.base_url, url, e)
                return

            print(self.index, kind, self.base_url, '->', url, 'okay')

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for key, value in attrs:
                if key == 'src':
                    url = urldefrag(urljoin(self.base_url, value))[0]

                    with seen_urls_lock:
                        seen = url in seen_urls
                        seen_urls.add(url)

                    if seen:
                        print(self.index, 'seen', self.base_url, '->', url)
                    else:
                        self.check_url('image', url)
        elif tag == 'a':
            for key, value in attrs:
                if key == 'href':
                    url = urldefrag(urljoin(self.base_url, value))[0]
                    parsed_url = urlparse(url)

                    with seen_urls_lock:
                        seen = url in seen_urls
                        seen_urls.add(url)

                    if seen:
                        print(self.index, 'seen', self.base_url, '->', url)
                    else:
                        if parsed_url.scheme == 'mailto':
                            pass
                        elif 'download.tinkerforge.com/' in url:
                            pass
                        elif 'tinkerforge.com/' in url:
                            if '/shop/customer/account/' in url:
                                pass
                            elif '/blog/' in url or '/blog?' in url and ignore_blog_errors:
                                pass
                            elif parsed_url.scheme == 'http':
                                if not ignore_http_usage:
                                    errors.put((self.base_url, url, 'http usage'))

                                    print(self.index, 'error', self.base_url, '->', url, 'http usage')
                            elif self.base_url != url:
                                if url.endswith('.jpg') or url.endswith('.png') or url.endswith('.gif') or url.endswith('.pdf'):
                                    self.check_url('local', url)
                                else:
                                    print(self.index, 'pending', pending_urls.qsize(), '+', url)
                                    pending_urls.put((self.base_url, url))
                        else:
                            self.check_url('external', url)

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass

def parse(index, base_url, url):
    retries = 3

    while True:
        try:
            with urlopen(url) as r:
                data = r.read().decode('utf-8')

            break
        except Exception as e:
            retries -= 1

            if retries >= 0:
                time.sleep(5)
                continue

            report_error(index, 'open', base_url, url, e)
            return

    Parser(index, url).feed(data)

def parse_loop(index):
    while True:
        base_url, url = pending_urls.get()

        print(index, 'open', base_url, '->', url)

        parse(index, base_url, url)

        pending_urls.task_done()

def error_loop():
    name = datetime.now().strftime('check_links_%Y%m%d_%H%M%S.log')

    with open(name, 'w') as f:
        pass

    while True:
        base_url, url, exception = errors.get()

        with open(name, 'a') as f:
            f.write('{0} -> {1} : {2}\n'.format(base_url, url, exception))

        errors.task_done()

threads = []

for index in range(200):
    thread = Thread(target=parse_loop, daemon=True, args=('{:03d}'.format(index),))
    thread.start()

    threads.append(thread)

thread = Thread(target=error_loop, daemon=True)
thread.start()

threads.append(thread)

try:
    pending_urls.join()
    errors.join()
except KeyboardInterrupt:
    pass
