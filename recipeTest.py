from recipe_scrapers import scrape_me

print("Please input url: ")
x="https://www.101cookbooks.com/pappardelle/"

# if link imported from https://www.xml-sitemaps.com/
x = x.split("2022")
x=x[0].rstrip()
print(x)
scraper = scrape_me(x)
print(scraper.title())
print(scraper.total_time())
print(scraper.ingredients())

