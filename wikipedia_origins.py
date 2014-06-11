import urllib
import urllib2
from bs4 import BeautifulSoup
import pandas as pd

def get_location(article):
    article = urllib.quote(article)
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')] #wikipedia needs this
    
    str_ret = ''
    try:
        resource = opener.open("http://en.wikipedia.org/wiki/" + article)
        data = resource.read()
        resource.close()
        soup = BeautifulSoup(data)

        # get birth
        try:
            str_ret = soup.find("th", text="Born").parent.find("a").get_text()
        except:
            str_ret = "Not Available"
        
        # get origin
        try:
            str_ret = str_ret + ' | ' + soup.find("th", text="Origin").parent.find("td").get_text()
        except:
            str_ret = str_ret + ' | ' + "Not Available"
        
    except:
        str_ret = "Artist not Found"
    
    return str_ret

if __name__ == "__main__":
  
  df = pd.read_csv('artists.csv')
  
  for x in df.T.iteritems():
    print x[1][0] + ' | ' + get_location(x[1][0])
