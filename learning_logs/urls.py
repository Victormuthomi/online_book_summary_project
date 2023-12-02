"""Define URLs for the learning_log"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns =[
    path('', views.index, name= 'index'),

    #A url that shows all the topics.
   path('topics/', views.topics, name ='topics'),
   path('topics/<int:topic_id>/', views.topic, name = 'topic'),

   # a page that allows a user to enter a topic
   path('new_topic/', views.new_topic, name = 'new_topic'),

   # a page for adding an entry on a specific topic
   path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
  
  #  A page for editing an entry
  path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),
]

