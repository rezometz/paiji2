# lancer avec :
# ../manage.py shell
# puis : execfile('update-iconsdb.py')
from forum.models import MessageIcon
from django.core.exceptions import *
from glob import glob

for j in glob('static/forum/icons/*.jpg') + glob('static/forum/icons/*.gif'):
    i = j.split('/').pop() 
    try:
        MessageIcon.objects.get(filename=i)
    except ObjectDoesNotExist:
        MessageIcon(name=i, filename=i).save()
        print "fichier {} ajoute".format(i)
    except MultipleObjectsReturned:
        print "{} n'est pas unique".format(i)
        raise
