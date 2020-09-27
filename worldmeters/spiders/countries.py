import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # Get all links in the country table
        countries = response.xpath("//td/a")
        # Loop, and get the country name and href link
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # absoulte_url = f"https://www.worldometers.info{link}"
            # absoulte_url = response.urljoin(link)

            # yield scrapy.Request(url=absoulte_url)
            # Follow the relative links
            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})

    def parse_country(self, response):
        # logging.info(response.url)
        name = response.request.meta['country_name']
        # Get the tabel that contain the year and population
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            yield {
                "country_name": name,
                "year": year,
                "population": population,
            }
