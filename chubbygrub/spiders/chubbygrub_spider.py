from chubbygrub.items import ChubbygrubItem
from scrapy.selector import Selector
import scrapy

class CategorySpider(scrapy.Spider):
	name = "chubbygrub"
	allowed_domains = ["chubbygrub.com"]
	
	start_urls = [
	"http://chubbygrub.com/categories/appetizers/",
	"http://chubbygrub.com/categories/breads/",
	"http://chubbygrub.com/categories/breakfast/",
	"http://chubbygrub.com/categories/breakfast-sandwiches/",
	"http://chubbygrub.com/categories/breakfast-tacos/",
	"http://chubbygrub.com/categories/burgers/",
	"http://chubbygrub.com/categories/burritos/",
	"http://chubbygrub.com/categories/chicken/",
	"http://chubbygrub.com/categories/coffee/",
	"http://chubbygrub.com/categories/cream-cheese-spreads/",
	"http://chubbygrub.com/categories/desserts/",
	"http://chubbygrub.com/categories/drinks/",
	"http://chubbygrub.com/categories/entrees/",
	"http://chubbygrub.com/categories/fajitas/",
	"http://chubbygrub.com/categories/french-fries/",
	"http://chubbygrub.com/categories/kids-meals/",
	"http://chubbygrub.com/categories/mexican-food/",
	"http://chubbygrub.com/categories/nuggets/",
	"http://chubbygrub.com/categories/paninis/",
	"http://chubbygrub.com/categories/pizzas/",
	"http://chubbygrub.com/categories/ribs/",
	"http://chubbygrub.com/categories/salads/",
	"http://chubbygrub.com/categories/sandwiches/",
	"http://chubbygrub.com/categories/seafood/",
	"http://chubbygrub.com/categories/shakes/",
	"http://chubbygrub.com/categories/sides/",
	"http://chubbygrub.com/categories/soups/",
	"http://chubbygrub.com/categories/tacos/",
	"http://chubbygrub.com/categories/tea/",
	"http://chubbygrub.com/categories/tortillas/",
	"http://chubbygrub.com/categories/wing-sauces/",
	"http://chubbygrub.com/categories/wings/",
	"http://chubbygrub.com/categories/wraps/"
	] 

	def parse(self, response): # Define parse() function. 

		items = [] # Element for storing scraped information.
		hxs = Selector(response) # Selector allows us to grab HTML from the response (target website).

		# Because we're using XPath language, we need to specify that the paragraphs we're trying to isolate are expressed via XPath.
		for sel in hxs.xpath("//table[@id='items']/tbody/tr"):

			item = ChubbygrubItem()

			item['name'] =  sel.xpath("td[1]/text()").extract() 
			item['restaurant']  =  sel.xpath("td[2]/a/text()").extract()
			item['calories'] = sel.xpath("td[3]/text()").extract()
			item['fat'] = sel.xpath("td[4]/text()").extract()
			item['carbs'] = sel.xpath("td[5]/text()").extract()
			item['actions'] = sel.xpath("td[6]/a[1]/@href").extract()

			items.append(item)
		return items # Shows scraped information as terminal output.