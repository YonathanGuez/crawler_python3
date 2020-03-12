import requests
from bs4 import BeautifulSoup


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

if __name__ == '__main__':
    url = 'https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    Syntaxlist = []

    for link in soup.find_all("meta"):
        #print(link.prettify())
        if link.get("name") != None:
            Syntaxlist.append(balise_analyse(link.get("name"),link.get("content", None), "checked"))
        if link.get("charset") != None:
            Syntaxlist.append(balise_analyse("charset", link.get("charset", None), "checked"))
        if link.get("scheme") != None:
            Syntaxlist.append(balise_analyse("scheme", link.get("scheme", None), "checked"))
        if link.get("property",None) == "og:title":
            Syntaxlist.append(balise_analyse("title", link.get("content", None), "checked"))
        if link.get("property", None) == "og:site_name":
            Syntaxlist.append(balise_analyse("site_name", link.get("content", None), "checked"))
        if link.get("property", None) == "og:url":
            Syntaxlist.append(balise_analyse("url", link.get("content", None), "checked"))
    for test in Syntaxlist:
        print(test)