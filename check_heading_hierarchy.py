# coding: utf-8
from bs4 import BeautifulSoup
import requests

class balise:
    def __init__(self, balise, text, res):
        self.balise = balise
        self.text = text
        self.res = res

def analyse_balise_h(child,  tuple):
    global tmp_hn, Syntaxlist
    if child.name in tuple:
        if tmp_hn != child.name:
            tmp_hn = child.name
        Syntaxlist.append(balise(child.name, child.text, "checked"))
    else:
        res = "Error syntaxe " + child.name + " need to be "+str(tuple)
        Syntaxlist.append(balise(child.name, child.text, res))

def scan_balise(test):
    hn = ("h1", "h2", "h3", "h4", "h5", "h6")
    child = test
    if child.name in hn:
        if tmp_hn == "":
            analyse_balise_h(child, ("h1"))
        elif tmp_hn == "h1":
            analyse_balise_h(child, ("h1", "h2"))
        elif tmp_hn == "h2":
            analyse_balise_h(child, ("h1", "h2", "h3"))
        elif tmp_hn == "h3":
            analyse_balise_h(child, ("h1", "h2", "h3", "h4"))
        elif tmp_hn == "h4":
            analyse_balise_h(child, ("h1", "h2", "h3", "h4", "h5"))
        elif tmp_hn == "h5":
            analyse_balise_h(child, ("h1", "h2", "h3", "h4", "h5", "h6"))
        elif tmp_hn == "h6":
            analyse_balise_h(child, ("h1", "h2", "h3", "h4", "h5", "h6"))

def search_balise(x):
    for child in x.children:
        if child.name != None:
           # print(child.name)
            scan_balise(child)
            search_balise(child)

if __name__ == '__main__':
   # url = 'http://sametmax.com/pourquoi-if-__name__-__main__-en-python/'
    url = 'https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python'
    page = requests.get(url)
    #with open("index.html", "r") as f:
    #    page = f.read()
    soup = BeautifulSoup(page.text, 'html.parser')
    tmp_hn = ""
    Syntaxlist = []
    search_balise(soup)
    print("***** Analyse des balise Hn: *****")
    verif = 0
    for obj in Syntaxlist:
        if obj.res != "checked":
            verif = 1
        print(obj.balise, obj.text, obj.res)
    if verif == 0:
        print("***** Good sementics Hn *****")
    else:
        print("***** Bad sementics Hn *****")
