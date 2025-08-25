# To activate the virtual environment --> scrapingEnv\Scripts\activate.bat
# Save this file in /wikiSpider/wikiSpider/ folder
# Perform the command => scrapy runspider Steelers_Super_Bowls.py to run this. 
# wikiSpider is the bot_name in the settings.py file
# Directory to run from is where the file is located
# Run scrapy runspider Steelers_Super_Bowls.py -o steeler_super_bowl_rosters.csv to create/append a csv file in the spiders folder
# Run scrapy runspider Steelers_Super_Bowls.py -O steeler_super_bowl_rosters.csv to create/overwrite a csv file in the spiders folder
# Run on \Web_Spiders\wikiSpider folder with command "scrapy crawl wikiSpider" to crawl through *.py files
# Change were made here, pipelines, items, and settings.py files


import scrapy
from wikiSpider.items import WikispiderItem

class SteelersSpider(scrapy.Spider):
    """
    Scrape the player rosters from the Pittsburgh Steeler Super Bowl wins
    """
    name = "steelers"
    allowed_domains = ['en.wikipedia.org']
    start_urls = [
        "https://en.wikipedia.org/wiki/Pittsburgh_Steelers",
    ]

    def parse(self, response):
        """
        Search for div tags with the class quote.
        Get the URL to the year the team won the superbowl
        """
        
        # Original XPath search written 
        #for link in response.xpath("//ul/li/a[contains(translate(@title, 'super bowl', 'SUPER BOWL'), 'SUPER BOWL')]"):
        #    preceding_a_tag = link.xpath('preceding-sibling::a[1]')       

        # New XPath search after reading a book
        for link in response.xpath('(//b/a[@title="History of the NFL championship"]/ancestor::td[@class="infobox-full-data"])/ul/li/a[contains(@href,"season")]'):
            link_text = link.xpath("@href").get()
            link_year = link.xpath("substring(@href,7,4)").get()
            if link_text:
                #print(link_text)
                #print(link_year)
                yield response.follow(link_text, meta={'year':link_year}, callback=self.super_bowl_team)

    def super_bowl_team(self, response):
        """
        Get the players from the Super Bowl Year roster
        """
        # Return the players from the season year and sotre in item class
        for player in response.xpath('//*[@id="Roster"]/following::table[1]/tbody/tr/td/ul/li/a'):
            player_name = player.xpath('text()').get()

            item = WikispiderItem()
            item['year'] =  response.meta.get('year')
            item['player'] =  player_name

            yield item
        

