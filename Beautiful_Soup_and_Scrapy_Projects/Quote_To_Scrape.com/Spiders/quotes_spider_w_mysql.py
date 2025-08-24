# To activate the virtual environment --> scrapingEnv\Scripts\activate.bat
# Save this file in /quotes_project/quotes_project/ folder
# Perform the command => scrapy runspider quotes_spider.py to run this. 
# quotes_spidir is the bot_name in the settings.py file
# Directory to run from is where the file is located
# Run scrapy runspider quotes_spider_w_mysql.py -o quotes.csv to create a csv file in the spiders folder
# Run on \Web_Spiders\quotes_project folder with command "scrapy crawl quotes" to crawl through *.py files
# Change were made here, pipelines, items, and settings.py files

import scrapy
from quotes_project.items import QuotesProjectItem

class QuotesSpider(scrapy.Spider):
    """
    Scrape the humor page of the author and quote
    """
    name = "quotes"
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [
        "https://quotes.toscrape.com/tag/humor/",
    ]

    def parse(self, response):
        """
        Search for div tags with the class quote.
        Get the author and text 
        """
        
        for quote in response.xpath("//div[@class='quote']"):
            item = QuotesProjectItem()
            item['author'] =  quote.xpath("span/small[@class='author']/text()").get(),
            item['text'] = quote.xpath("span[@class='text']/text()").get(),
            
            yield item

        # If there is a "next page" link follow the link and parse the data on that page too
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        print(f"Next page value is: {next_page}")
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        
        

