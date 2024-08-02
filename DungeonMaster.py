from random import randint
import requests
from bs4 import BeautifulSoup
# Library for opening url and creating
# requests
import urllib.request
# pretty-print python data structures
from pprint import pprint
# for parsing all the tables present
# on the website
from html_table_parser.parser import HTMLTableParser
# for converting the parsed data in a
# pandas dataframe
import pandas as pd
pd.set_option('display.max_columns', None) # problem with overflow
pd.set_option('display.max_rows', None) # problem wtih overflow
pd.set_option('display.max_colwidth', None)

def roll(input):
    pos = input.index("d")
    num = int(input[:pos])
    type = int(input[pos+1:])
    result = 0
    output = ""
    print(num)
    print(type)
    for x in range(num):
        die = randint(1,type)
        result += die
        output += f"{die} "

    return f"{output}= {result}"

def add(arr):
    result = 0
    for i in arr:
        result += int(i)
    return result

def wiki():
    r = requests.get('http://dnd5e.wikidot.com/')
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_="col-lg-5 col-md-6")
    content = s.find_all("p")
    return content

#from gitlab
## Text splitting
def rightTrim(text, toBeTrimmed):
    while text.endswith(toBeTrimmed):
        text = text[:-len(toBeTrimmed)]
    return text

def splittingIndex(text, maxLength, newline):
    if len(text) <= maxLength:
        return(len(text))
    remainingText = text[:maxLength+2*len(newline)]
    while True:
        possibleIndex = remainingText.rindex(newline)
        remainingText = remainingText[:possibleIndex]
        if remainingText.endswith(newline):
            remainingText = rightTrim(remainingText, newline)
        elif possibleIndex <= maxLength:
            return possibleIndex

def split(text, maxLength, newline):
    splittedText = []
    while text != "":
        currentSplittingIndex = splittingIndex(text, maxLength, newline)
        splittedText.append(text[:currentSplittingIndex])
        text = text[currentSplittingIndex+len(newline):]
    return splittedText

def scrapeSpell(input):
    url = "http://dnd5e.wikidot.com/spell:"
    url += input
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_="main-content")
    content = s.find_all(["p", "ul", "tr"])

    return content

def scrapeFeat(input):
    url = "http://dnd5e.wikidot.com/feat:"
    url += input
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_="main-content")
    content = s.find_all(["p", "ul", "tr"])
    return content

def scrapeRace(input):
    url = "http://dnd5e.wikidot.com/lineage:"
    url += input
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    s = soup.find('div', class_="main-content")
    content = s.find_all(["p", "ul", "tr"])
    return content

def scrapeClass(input):
    url = "http://dnd5e.wikidot.com/"
    url += input

    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)

    contents = f.read()

    xhtml = contents.decode('utf-8')

    p = HTMLTableParser()

    p.feed(xhtml)

    db = pd.DataFrame(p.tables[0])
    if (input == "wizard" or input == "cleric" or input == "druid" or input == "bard" or input == "warlock"):
        part1 = db.iloc[:10, :3]  # first half of rows
        part2 = db.iloc[10:, :3]  # first half of rows
        part3 = db.iloc[:, 3:]  # second half of rows
    else:
        part1 = db.iloc[:10, :3]  # first half of rows
        part2 = db.iloc[10:, :3]  # first half of rows
        part3 = db.iloc[:, 3:]  # second half of rows

    toReturn = [part1, part2, part3]

    return(toReturn)

scrapeClass("wizard")