import random

def makePoem():

    string=[]

    a = random.choice(nouns)
    b = random.choice(nouns)
    while a==b:
        b = random.choice(nouns)
    c = random.choice(nouns)
    while b==c:
        c = random.choice(nouns)
    string.append(a)
    string.append(b)
    string.append(c)

    a = random.choice(verbs)
    b = random.choice(verbs)
    while a==b:
        b = random.choice(verbs)
    c = random.choice(verbs)
    while b==c:
        c = random.choice(verbs)
    string.append(a)
    string.append(b)
    string.append(c)

    a = random.choice(adjectives)
    b = random.choice(adjectives)
    while a==b:
        b = random.choice(adjectives)
    c = random.choice(adjectives)
    while b==c:
        c = random.choice(adjectives)
    string.append(a)
    string.append(b)
    string.append(c)

    a = random.choice(adverbs)
    string.append(a)

    a = random.choice(prepositions)
    b = random.choice(prepositions)
    while a==b:
        b = random.choice(adjectives)
    string.append(a)
    string.append(b)

    if "aeiou".find(string[6][:1]) == -1:
        adjusted = "A"
    else:
        adjusted = "An"

    string.append(adjusted)
    
    return string


    


if __name__ == '__main__':

    nouns = ['fossil', 'horse', 'aardvark', 'judge', 'chef', 'mango', 'extrovert','gorilla', 'apple']
    verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
    adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
    prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over","within"]
    adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]
    
    listing = makePoem()
    print ("{} {} {}".format(listing[12],listing[6],listing[0]))
    print ("")

#{A/An} {adjective1} {noun1}
#{A/An} {adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2}
#{adverb1}, the {noun1} {verb2}
#the {noun2} {verb3} {preposition2} a {adjective3} {noun3}
