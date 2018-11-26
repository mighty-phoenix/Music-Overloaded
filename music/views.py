from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models import Q
from .models import Playlist, Song
from .forms import PlaylistForm, SongForm, UserForm

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        playlists = Playlist.objects.filter(user=request.user)
        song_results = Song.objects.all()
        query = request.GET.get("q")
        if query:
            playlists = playlists.filter(
                Q(title__icontains=query) 
                ).distinct()
            song_results = song_results.filter(
                Q(song_title__icontains=query)
            ).distinct()
            return render(request, 'music/index.html', {
                'playlists': playlists,
                'songs': song_results,
            })
        else:
            return render(request, 'music/index.html', {'playlists': playlists}, {'songs': song_results})


def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
          if user.is_active:
              login(request, user)
              playlists = Playlist.objects.filter(user=request.user)
              return render(request,'music/index.html',{'playlists': playlists})
          else:
              return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')

def viewall(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        song_results = Song.objects.all()
        return render(request, 'music/viewall.html', {
            'songs': song_results,
        })
        
def detail(request, playlist_id):

    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        user = request.user
        playlist = get_object_or_404(Playlist, pk=playlist_id)
        return render(request, 'music/detail.html', {'playlist': playlist, 'user': user})


def favorite(request, song_id):

    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def favorite_playlist(request, playlist_id):

    playlist = get_object_or_404(Playlist, pk=playlist_id)
    try:
        if playlist.is_favorite:
            playlist.is_favorite = False
        else:
            playlist.is_favorite = True
        playlist.save()
    except (KeyError, Playlist.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def songs(request, filter_by):

    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        try:
            song_ids = []
            for playlist in Playlist.objects.filter(user=request.user):
                for song in playlist.song_set.all():
                    song_ids.append(song.pk)
            users_songs = Song.objects.filter(pk__in=song_ids)
            if filter_by == 'favorites':
                users_songs = users_songs.filter(is_favorite=True)
        except Playlist.DoesNotExist:
            users_songs = []
        return render(request, 'music/songs.html', {
            'song_list': users_songs,
            'filter_by': filter_by,
        })


def logout_user(request):

    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)


def register(request):

    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                playlists = Playlist.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'playlists': playlists})
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)


def create_playlist(request):

    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        form = PlaylistForm(request.POST or None)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.user = request.user
            playlist.save()
            return render(request,'music/detail.html',{'playlist': playlist})
        context = {
            "form": form
        }
        return render(request, 'music/create_playlist.html', context)


def create_song(request, playlist_id):

    form = SongForm(request.POST or None, request.FILES or None)
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    if form.is_valid():
        playlists_songs = playlist.song_set.all()
        for s in playlists_songs:
            if s.song_title == form.cleaned_data.get("song_title"):
                context = {
                    'playlist': playlist,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'music/create_song.html', context)
        song = form.save(commit=False)
        song.playlist = playlist
        song.audio_file = request.FILES['audio_file']
        file_type = song.audio_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in AUDIO_FILE_TYPES:
            context = {
                'playlist': playlist,
                'form': form,
                'error_message': 'Audio file must be WAV, MP3, or OGG',
            }
            return render(request, 'music/create_song.html', context)

        song.save()
        return render(request, 'music/detail.html', {'playlist': playlist})
    context = {
        'playlist': playlist,
        'form': form,
    }
    return render(request, 'music/create_song.html', context)


def delete_playlist(request, playlist_id):

    playlist = Playlist.objects.get(pk=playlist_id)
    playlist.delete()
    playlists = Playlist.objects.filter(user=request.user)
    return render(request, 'music/index.html', {'playlists': playlists})


def delete_song(request, playlist_id, song_id):

    playlist = get_object_or_404(Playlist, pk=playlist_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'music/detail.html', {'playlist': playlist})


def newsfeed(request): #Execution of syndcation
    return render(request,"music/rss.html",{})
















