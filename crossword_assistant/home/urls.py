from django.conf.urls import url
from . import views
urlpatterns = [
      url(r'^$', views.index, name='index' ),
      url(r'^clue$' ,views.clueinput, name='clueinput'),
      url(r'^finish$',views.finish,name='finish'),
      url(r'^answer$',views.answer,name='answer'),
      url(r'^solve$',views.solve,name='solve'),
      url(r'^clear$',views.empty_table,name='new_crossword'),
      url(r'^solve_all$',views.solve_all,name='solve_all')
    ]
