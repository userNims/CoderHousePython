from django import forms

class Playlist_form(forms.Form):
    nombre_cancion=forms.CharField(max_length=50)
    artista=forms.CharField(max_length=50)
    album=forms.CharField(max_length=50)

class Artista_form(forms.Form):
    nombre_completo=forms.CharField(max_length=50)
    nacionalidad=forms.CharField(max_length=50)
    arte=forms.CharField(max_length=50)

class Album_form(forms.Form):
    nombre_album=forms.CharField(max_length=50)
    creador=forms.CharField(max_length=50)
    año=forms.IntegerField()