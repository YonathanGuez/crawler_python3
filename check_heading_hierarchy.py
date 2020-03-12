# coding: utf-8
from bs4 import BeautifulSoup
import requests

class balise_analyse:
    def __init__(self, balise, text, res=""):
        self.balise = balise
        self.text = text
        self.nb_char = len(self.text)
        self.listword = self.text.split()
        self.nb_word = len(self.listword)
        self.res_char = ""
        self.analysebalise()
        self.res_hierarchy = res

    def analysebalise(self):
        hn = ("h1", "h2", "h3", "h4", "h5", "h6")
        if self.balise == "title":
            if self.nb_char < 65:
                self.res_char = "ok"
            else:
                self.res_char = "Error > 70 char"
        if self.balise == "description":
            if (self.nb_char < 230) and (self.nb_char > 154):
                self.res_char = "ok but google decide"
            elif self.nb_char <= 154:
                self.res_char = "old school limit 154 good for target your information"
            else:
                self.res_char = "Error > 154 char "
        if self.balise == "keywords":
                self.res_char = "google not use this"

        if self.balise == "charset":
                self.res_char = "we have one charset"

        if self.balise == "site_name":
            self.res_char = "need to check"

        if self.balise == "url":
            self.res_char = "need to check"

        if self.balise == "robots":
            self.res_char = "need to check"

        if self.balise == "syndication-source":
            self.res_char = "need to check"

        if self.balise == "original-source":
            self.res_char = "need to check"

        if self.balise in hn:
            if self.nb_char < 70:
                self.res_char ="ok"
            else:
                self.res_char = "Error > 70 char"

    def __str__(self):
        """Méthode affichage objet"""
        return "{}|{}|{}|{}|{}".format(
            self.balise, self.text, self.nb_char,
            self.nb_word, self.res_char, self.res_hierarchy)

class AnalyseHeading:
    def __init__(self, url):
        self.url = url
        self.Syntaxlist_hn = []
        self.tmp_hn = ""
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, 'html.parser')
        self.search_balise(self.soup)

    def search_balise(self, x):
        for child in x.children:
            if child.name != None:
                self.scan_balise(child)
                self.search_balise(child)

    def analyse_balise_h(self, child, tuple):
        if child.name in tuple:
            if self.tmp_hn != child.name:
                self.tmp_hn = child.name
            self.Syntaxlist_hn.append(balise_analyse(child.name, child.text, "checked"))
        else:
            res = "Error syntaxe " + child.name + " need to be "+str(tuple)
            self.Syntaxlist_hn.append(balise_analyse(child.name, child.text, res))

    def scan_balise(self,test):
        hn = ("h1", "h2", "h3", "h4", "h5", "h6")
        child = test
        if child.name in hn:
            if self.tmp_hn == "":
                self.analyse_balise_h(child, ("h1"))
            elif self.tmp_hn == "h1":
                self.analyse_balise_h(child, ("h1", "h2"))
            elif self.tmp_hn == "h2":
                self.analyse_balise_h(child, ("h1", "h2", "h3"))
            elif self.tmp_hn == "h3":
                self.analyse_balise_h(child, ("h1", "h2", "h3", "h4"))
            elif self.tmp_hn == "h4":
                self.analyse_balise_h(child, ("h1", "h2", "h3", "h4", "h5"))
            elif self.tmp_hn == "h5":
                self.analyse_balise_h(child, ("h1", "h2", "h3", "h4", "h5", "h6"))
            elif self.tmp_hn == "h6":
                self.analyse_balise_h(child, ("h1", "h2", "h3", "h4", "h5", "h6"))

    def show_analyse(self):
        print("***** Analyse des balise Hn: *****")
        verif = 0
        for obj in self.Syntaxlist_hn:
            if obj.res_hierarchy != "checked":
                verif = 1
            print(obj.balise, obj.text + ":Nb=" + (str(obj.nb_char)), obj.res_hierarchy)
        if verif == 0:
            print("***** Good sementics Hn *****")
        else:
            print("***** Bad sementics Hn *****")

if __name__ == '__main__':
   # url = 'http://sametmax.com/pourquoi-if-__name__-__main__-en-python/'
    url = 'https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python'
    analyse = AnalyseHeading(url)
    analyse.show_analyse()
