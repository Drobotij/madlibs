import spacy
import requests
import json

print("!Welcome to MadLibs¡ \nBreaking Bad quotes.")

#makes the GET call to the API
endpoint = "https://breaking-bad-quotes.herokuapp.com/v1/quotes"
respons = requests.get(endpoint)

#gets the phrase and the author
data = json.loads(respons.content)
phrase = data[0]["quote"]
author = data[0]["author"]


nlp = spacy.load("en_core_web_md")
doc = nlp(phrase)

#gets the verbs and nouns from the phrase and store them in lists
verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
nouns = [chunk.text for chunk in doc.noun_chunks]

#variable and lists declaration and initialization
newVerbs = []
newNouns = []
newFrace = phrase

if len(verbs) > 0: #checks that the phrase has verbs
    print("We need {} verbs".format(len(verbs)))
    for i in range(len(verbs)):#store all verbs that are inputed by the user in newVerbs
        newVerbs.append(input("Enter verb n°{}: ".format(i  + 1)))

if len(nouns) > 0:#checks that the phrase has nouns
    print("Now, we need {} nouns".format(len(nouns)))
    for i in range(len(nouns)):#store all nouns that are inputed by the user in newVerbs
        newNouns.append(input("Enter noun n°{}: ".format(i + 1)))

#replace verbs and nouns in the phrase
for i in range(len(newVerbs)):
    newFrace = newFrace.replace(verbs[i], newVerbs[i])
    
for i in range(len(newNouns)):
    newFrace = newFrace.replace(nouns[i], newNouns[i])
#---


#show results

print("\nPerfect! These are the results: \n")

print("Original frace: ")
print("{} - {}".format(phrase,author))

print("\nNew frase: ")
print("{} - {}".format(newFrace, author))