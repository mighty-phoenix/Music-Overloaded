from django import forms
from django.contrib.auth.models import User

from .models import Playlist, Song

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title','audio_file']


class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ['title']
