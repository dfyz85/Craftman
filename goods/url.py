'''
Created on 12.05.2011

@author: dfyz
'''
from django.conf.urls.defaults import *

urlpatterns = patterns('Craftman.goods.views',
                        url(r'^$', 'menu_text'), 
                        url(r'^start/$','english_rusian'),
                        )