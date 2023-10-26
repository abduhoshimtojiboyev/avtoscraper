BOT_NAME = "car"

SPIDER_MODULES = ["car.spiders"]
NEWSPIDER_MODULE = "car.spiders"

FEEDS = {
    'carsdata1.csv': {'format': 'csv'},
}


SCRAPEOPS_API_KEY = 'YOUR_SCRAPEOPS'
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'http://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
SCRAPEOPS_NUM_RESULTS = 50

ROTATING_PROXY_LIST = [
    'IP_PROXY:PORT',
    'IP_PROXY:PORT',
    '.',
    '.'
]

# ROTATING_PROXY_LIST_PATH = '..\Free_Proxy_List.txt'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False


# Add download delay in ip requests in order to not getting blocked by website
DOWNLOAD_DELAY = 5

DOWNLOADER_MIDDLEWARES = {
    "car.middlewares.ScrapeOpsFakeBrowserHeaderAgentMiddleware": 400,
    # 'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 800,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 800,
}


# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

