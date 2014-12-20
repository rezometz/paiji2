from django import template
from django.core.cache import get_cache
from django.conf import settings

from bs4 import BeautifulSoup
import urllib2

register = template.Library()

def fetchFTPs():
<<<<<<< HEAD
    response = urllib2.urlopen('http://porygon.rez', timeout=1).read()
    soup = BeautifulSoup(response)
    ftps = []
    for ftp in soup.select('#ftp_list a'):
        ftps.append({
            'name': ftp.text,
            'link': ftp.get('href')
            })
=======
    ftps = []
    try:
        response = urllib2.urlopen('http://porygon.rez', timeout=1).read()
        soup = BeautifulSoup(response)
        for ftp in soup.select('#ftp_list a'):
            ftps.append({
                'name': ftp.text,
                'link': ftp.get('href')
                })
    except urllib2.URLError:
        pass
>>>>>>> ff11b318f416cd17afff37561e23ab5487cadb52
    return ftps

@register.inclusion_tag('home/ftps_list.html')
def get_ftps():
    cache = get_cache('default')
    ftps = cache.get(settings.KEY_CACHE_FTPS)
    if ftps is None:
<<<<<<< HEAD
		try:
			ftps = fetchFTPs()
		except : #URLError:
			#in case of porygon being unreachable
			ftps = [{
				'name': "Porygon unreachable",
				'link': "htpp://paiji.rez"
				}]
        #Cache ftps info for 25 min
		cache.set(settings.KEY_CACHE_FTPS, ftps, 60*25)
=======
        ftps = fetchFTPs()
        # Cache ftps info for 25 min
        cache.set(settings.KEY_CACHE_FTPS, ftps, 60*25)
>>>>>>> ff11b318f416cd17afff37561e23ab5487cadb52
    return {'ftps': ftps}
