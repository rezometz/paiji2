from forum.models import MessageIcon
from django.core.exceptions import *
from glob import glob

def update_icons_db():
    for j in glob('forum/static/forum/icons/*.jpg') + glob('forum/static/forum/icons/*.gif'):
        i = j.split('/').pop() 
        try:
            MessageIcon.objects.get(filename=i)
        except ObjectDoesNotExist:
            MessageIcon(name=i, filename=i).save()
            print "fichier {} ajoute".format(i)
        except MultipleObjectsReturned:
            print "{} n'est pas unique".format(i)
            raise

update_icons_db()
