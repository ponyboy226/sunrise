import sys
import urllib2
from bs4 import BeautifulSoup

state = str(raw_input('What state? '))
city = str(raw_input('Which city in {0}? '.format(state)))


def sunWatcher(city, state):
    url = 'http://www.gaisma.com/en/location/{0}-{1}.html'.format(city, state)
    html_doc = urllib2.urlopen(url)
    soup = BeautifulSoup(html_doc.read())
    today = soup.find_all('td', {'class' : 'sdlh'})[0].get_text()
    todayTime = soup.find_all('td', {'class' : 'dawn'})[0].get_text()
    tomorrowTime = soup.find_all('td', {'class' : 'dawn'})[1].get_text()


    print("\n\n%s in %s the sun rose at %sam\n\nTomorrow, the sun will rise at %sam\n\n" %(today, city.capitalize(), todayTime, tomorrowTime))
    
if __name__ == '__main__':
    try:
        sunWatcher(city, state)
        #sunWatcher(sys.argv[1])
    except IndexError:
        print "Please enter a valid city and state name"