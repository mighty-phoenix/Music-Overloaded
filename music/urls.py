from django.conf.urls import url
from . import views
app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^viewall/$', views.viewall, name='viewall'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<playlist_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    url(r'^add_playlist/$', views.add_playlist, name='add_playlist'),
    url(r'^(?P<playlist_id>[0-9]+)/add_song/$', views.add_song, name='add_song'),
    url(r'^(?P<playlist_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^(?P<playlist_id>[0-9]+)/favorite_playlist/$', views.favorite_playlist, name='favorite_playlist'),
    url(r'^(?P<playlist_id>[0-9]+)/delete_playlist/$', views.delete_playlist, name='delete_playlist'),
    url(r'^newsfeed/$', views.newsfeed, name='newsfeed')
]

   
    
