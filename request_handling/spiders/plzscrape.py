import scrapy

# This spider will return the headers of the request
class HeaderSpider(scrapy.Spider):
    name = "headerspider"
    allowed_domains = ["httpbin.io"]
    start_urls = ["https://httpbin.io/headers"]

    def start_requests(self):
        #alter header
        custom_headers = {
            "Sec-Ch-Ua-Platform": "\"Linux\"",
        }

        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, headers=custom_headers, cookies={'country': 'USA'})

    def parse(self, response):
        yield {
            'data': response.json()
        }

# This spider will return submitted cookies
class CookieSpider(scrapy.Spider):
    name = "cookiespider"
    allowed_domains = ["httpbin.io"]
    start_urls = ["https://httpbin.io/cookies"]

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, cookies={'country': 'USA'})

    def parse(self, response):
        yield {
            'data': response.json()
        }

# This spider will return a 500 status code
class HTTP500Spider(scrapy.Spider):
    name = "http500spider"
    allowed_domains = ["httpbin.io"]
    start_urls = ["https://httpbin.io/status/500"]

    def parse(self, response):
        yield {
            'data': response.status
        }

# This spider will return a 404 status code
class HTTP404Spider(scrapy.Spider):
    name = "http404spider"
    allowed_domains = ["httpbin.io"]
    start_urls = ["https://httpbin.io/status/404"]

    def parse(self, response):
        yield {
            'data': response.status
        }

# This spider will return a 403 status code
class HTTP400Spider(scrapy.Spider):
    name = "http400spider"
    allowed_domains = ["httpbin.io"]
    start_urls = ["https://httpbin.io/status/400"]

    def parse(self, response):
        yield {
            'data': response.status
        }

#not handled by default. this spider will fail
class HTTP403Spider(scrapy.Spider):
    name = "http403spider"
    allowed_domains = ["httpbin.io"]
    start_urls = ["https://httpbin.io/status/403"]

    def parse(self, response):
        yield {
            'data': response.status
        }