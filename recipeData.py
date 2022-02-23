from recipe_scrapers import scrape_me

lines = [line.rstrip('\n') for line in open("recipes/"+"bonappetit"+".txt")]
f=open("recipes/recipelinks2.txt","w")

for each in lines:

    # links imported from https://www.xml-sitemaps.com/
    each = each.split("2022")
    each=each[0].rstrip()

    if ".com/recipe/" in "".join(lines):
        if ".com/recipe/" not in each:
            continue
    try:
        scraper = scrape_me(each)
        ingredients=",,".join(scraper.ingredients())
        st=scraper.total_time()
        f.write(each+"|"+scraper.title()+"|"+str((st if st!=None else "0"))+"|"+ingredients)
        f.write("\n")
        print(each)
    except:
        continue
f.close()
