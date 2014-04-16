from bs4 import BeautifulSoup
import urllib2


def get_word(date):
    page = urllib2.urlopen("http://dictionary.reference.com/wordoftheday/archive/"+date+".html")

    soup = BeautifulSoup(page)

    word = soup.find_all("h2", "me")[0].get_text().encode('ascii', 'ignore')
    defns = []
    for defn in soup.find_all("div", "defn"):
        defns.append(defn.get_text().strip().replace('\n', '').encode('ascii', 'ignore'))

    return [word, defns]


def get_week_words():
    words = []
    from datetime import date, timedelta
    for i in range(10):
        dt = date.today() - timedelta(i*i*i)
        words.append(get_word(dt.strftime('%Y/%m/%d')))

    return words
