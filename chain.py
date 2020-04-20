import random
import json
import os
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')


def preprocess(text):
    return " ".join(tokenizer.tokenize(text)).lower()

def GetPairs(text, phraseLen):
    if type(text) != type([]) and type(text) != type(""):
        raise ValueError(f"{text.__class__.__name__} type doesn't supported".capitalize())
    if type(text) == type(""):
        arrayWords = text.split()
    if type(text) == type([]):
        arrayWords = text.copy()
    arrayWords += ["*END*"] * phraseLen
    arrayPairs = []
    for indexOfFirst in range(len(arrayWords) - phraseLen * 2 + 1):
        arrayPairs.append([" ".join(arrayWords[indexOfFirst:indexOfFirst + phraseLen]), 
                           " ".join(arrayWords[indexOfFirst + phraseLen:indexOfFirst + phraseLen + phraseLen])])
    return arrayPairs

def GenChains(text, phraseLen):
    chainsRaw = GetPairs(text, phraseLen)
    chains = {}
    for chainRaw in chainsRaw:
        if chainRaw[0] in chains:
            if not chainRaw[1] in chains[chainRaw[0]]:
                chains[chainRaw[0]].append(chainRaw[1])
        else:
            chains[chainRaw[0]] = []
            chains[chainRaw[0]].append(chainRaw[1])
    return chains

def GenText(chains, limit = -1):
    counter = 0
    text = ""
    currentWord = random.choice(list(chains.keys()))
    while True:
        currentWord = chains[currentWord][random.randint(0, len(chains[currentWord]) - 1)]
        if "*END*" in currentWord or (counter >= limit and limit > 0):
            text = text[:-1]
            break
        text += currentWord + " "
        counter += 1
    return text

def SaveChains(artist, chainName, chains):
    with open(f'chains/{artist}_{chainName}.txt', 'w', encoding="utf8") as outfile:
        json.dump(chains, outfile)

def LoadChains(artist, chainName):
    if os.path.isfile('filename.txt'):
        with open(f'chains/{artist}_{chainName}.txt', 'r', encoding="utf8") as outfile:
            return json.load(outfile)
    else:
        SaveChains(artist, chainName, chains)
        with open(f'chains/{artist}_{chainName}.txt', 'r', encoding="utf8") as outfile:
            return json.load(outfile)

        
def SendPunch():
    return GenText(LoadChains(artist, chainName), textLen)

artist = "oxxxymiron"
chainName = "general"
textLen = 64

InputText = open("battle-mc/oxxxymiron.txt", "r", encoding="utf8").read()

chains = GenChains(f"{preprocess(InputText)} *END*", 1)