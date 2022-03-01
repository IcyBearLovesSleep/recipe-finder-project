# recipe finder 

# Format a time in a human readable format.
def tformat(mins):
    mins=int(mins)
    times = [("hr", 60),("min", 1)]
    if not mins:
        return ""
    time = []
    for i, j in times:
        qty = mins // j
        if qty:
            if qty > 1:
                i += "s"
            time.append(str(qty) + " " + i)
        mins %= j
    return ' '.join(time)

import json
recipes = json.load(open("recipes.json","r"))
recipes=recipes['recipes']

# Open a history. txt file.
history = open("history.txt","a")

#ingredients included by default, optional for neglection
defaults = ['ice', 'water', 'oil', 'salt', 'pepper', 'sugar', 'butter', 'optional']

print("Please input your food (separated by ',')\n(" + ", ".join([i for i in defaults if i != "optional"]) + " are included by default.)")
food = input("food: ")
foodlist = [i.strip() for i in food.split(",")]

recipesVal = 0
titles=[]
times=[]
matches_size=[]
links=[]

for title in recipes:
    matches = []
    matchLen = 0
    reci=recipes[title]
    for ingred in reci['ingredients']:
        ingred = ingred.lower()
        #ingredient matches
        if any(i in ingred for i in foodlist):
            for i in foodlist:
                if i in ingred:
                    matches.append(i)
                    matchLen += 1
                    break

        #default ingredients that are ignored (like water, sugar, salt etc.)
        elif any(i in ingred for i in defaults):
            for i in defaults:
                if i in ingred:
                    matchLen += 1
                    break

    #if every ingredient in the recipe has a corresponding match
    if matchLen == len(reci['ingredients']) and len(matches) > 0:

        titles.append(title)
        times.append(tformat(reci['time']))
        matches_size.append(matches)
        links.append(reci['link'])
        recipesVal += 1
print("We've found " + str(recipesVal) + " recipe results!\n")
history.write(",".join(foodlist)+"\n")
history.close()
for i,j,k,h in zip(titles, times, matches_size, links):
    print(i + "    " + j)
    k=list(dict.fromkeys(k))
    print(str(len(k)) + " ingredients used: " + ", ".join(k))
    print(h, "\n")