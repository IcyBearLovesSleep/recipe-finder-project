from recipe_scrapers import scrape_me
lines = [line.rstrip('\n') for line in open('recipeLinks.txt')]

f = open('recipes.json','w')
f.write('{\n')
f.write('  "recipes" : {\n')

recipesValid = 0
recipesTotal = 0

for each in lines:
    each=each.split("|")
    each=each[0]
    try:
        scraper = scrape_me(each)
        ingreds =  [i.replace('"',"''") for i in scraper.ingredients()]
        
        title = scraper.title().replace('"',"'")
        
        st=scraper.total_time()
        f.write(',\n    "' + title + '": {\n')
        f.write('      "ingredients": ["' + '", "'.join(ingreds) + '"],\n')
        f.write('      "time": ' + str(st if st!=None else 0) + ',\n')
        f.write('      "link":"' + each + '"\n')
        f.write('    }')
        print(each)
    except:
        continue
    
		
f.write('\n  }\n}')
f.close()	