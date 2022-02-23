# recipe finder 

def tformat(x):
    if isinstance(x, int):
        x=str(x)
    if int(x)<0:
        return "invalid time"
    elif x=="0":
        return ""
    elif x=="1":
        return "1 min"
    elif 1<int(x)<60:
        return x+" mins"
    elif x=="60":
        return "1 hr"
    elif 120>int(x)>60:
        return "1 hr " +str(int(x)%60)+" mins"
    elif int(each[2])>120 and int(each[2])%60!=0:
        return str(int(each[2])//60)+" hrs " +str(int(each[2])%60)+" mins"
    elif int(each[2])>60 and int(each[2])%60==0:
        return str(int(each[2])//60)+" hrs "

lines = [i.rstrip("\n") for i in open('recipeLinks.txt', encoding="utf8", errors="replace")]

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

for each in lines:
    each=each.split("|")
    ingreds = each[3].split(",,")
    matches = []
    matchLen = 0
    for ingred in ingreds:
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
    if matchLen == len(ingreds) and len(matches) > 0:

        titles.append(each[1])
        times.append(tformat(each[2]))
        matches_size.append(matches)
        links.append(each[0])
        recipesVal += 1
print("We've found " + str(recipesVal) + " recipe results!\n")
history.write(",".join(foodlist)+"\n")
history.close()
for i,j,k,h in zip(titles, times, matches_size, links):
    print(i + "    " + j)
    k=list(dict.fromkeys(k))
    print(str(len(k)) + " ingredients used: " + ", ".join(k))
    print(h, "\n")