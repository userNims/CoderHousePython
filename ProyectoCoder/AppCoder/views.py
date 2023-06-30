from django.shortcuts import render
import email
from AppCoder.models import Playlist, Artista, Album
from django.http import HttpResponse
from django.template import Context, Template, loader
from datetime import datetime
from AppCoder.forms import Playlist_form, Artista_form, Album_form

def album(request):
    return render (request, "AppCoder/album.html")

def artista(request):
    return render(request, "AppCoder/artista.html")

def playlist(request):
    return render (request, "AppCoder/playlist.html")

def inicio(request):
    return render (request, "AppCoder/inicio.html")

#PLAYLIST
def playlist_formulario(request):
    if (request.method=="POST"):
        form=Playlist_form(request.POST)
        if form.is_valid():
            info= form.cleaned_data #dicc con la info sin lo demás
            nombre_cancion=info["nombre_cancion"]
            artista=info["artista"]
            album=info["album"]
            playlist=Playlist(nombre_cancion=nombre_cancion, artista=artista, album=album)
            playlist.save()
            return render (request, "AppCoder/inicio.html")
    else: #sino viene por GET
        form=Playlist_form() #creo el form vacío
    return render(request, "AppCoder/playlist_formulario.html", {"formulario":form}) #lo renderizo y se lo mando como un dicc para que lo pueda usar la template

def busqueda_cancion(request):
    return render(request, "AppCoder/busqueda_cancion.html")

def buscar_cancion(request):
    if request.GET["nombre_cancion"]:
        nombre_cancion=request.GET["nombre_cancion"]
        canciones=Playlist.objects.filter(nombre_cancion__icontains=nombre_cancion)
        return render(request, "AppCoder/resultados_busqueda_cancion.html", {"canciones":canciones})
    else:
        return render(request, "AppCoder/busqueda_cancion.html", {"error": "No se ingresó ninguna canción"})


#ARTISTA
def artista_formulario(request):
    if (request.method=="POST"):
        form=Artista_form(request.POST)
        if form.is_valid():
            info= form.cleaned_data #dicc con la info sin lo demás
            nombre_completo=info["nombre_completo"]
            nacionalidad=info["nacionalidad"]
            arte=info["arte"]
            artistas=Artista(nombre_completo=nombre_completo, nacionalidad=nacionalidad, arte=arte)
            artistas.save()
            return render (request, "AppCoder/inicio.html")
    else: #sino viene por GET
        form=Artista_form() #creo el form vacío
    return render(request, "AppCoder/artista_formulario.html", {"formulario":form}) #lo renderizo y se lo mando como un dicc para que lo pueda usar la template

def busqueda_artista(request):
    return render(request, "AppCoder/busqueda_artista.html")

def buscar_artista(request):
    if request.GET["nombre_completo"]:
        nombre_completo=request.GET["nombre_completo"]
        artistas=Artista.objects.filter(nombre_completo__icontains=nombre_completo)
        return render(request, "AppCoder/resultados_busqueda_artista.html", {"artistas":artistas})
    else:
        return render(request, "AppCoder/busqueda_artista.html", {"error": "No se ingresó ningún artista con ese nombre"})


#ALBUM
def album_formulario(request):
    if (request.method=="POST"):
        form=Album_form(request.POST)
        if form.is_valid():
            info= form.cleaned_data #dicc con la info sin lo demás
            nombre_album=info["nombre_album"]
            creador=info["creador"]
            año=info["año"]
            albums=Album(nombre_album=nombre_album, creador=creador, año=año)
            albums.save()
            return render (request, "AppCoder/inicio.html")
    else: #sino viene por GET
        form=Album_form() #creo el form vacío
    return render(request, "AppCoder/album_formulario.html", {"formulario":form}) #lo renderizo y se lo mando como un dicc para que lo pueda usar la template

def busqueda_album(request):
    return render(request, "AppCoder/busqueda_album.html")

def buscar_album(request):
    if request.GET["nombre_album"]:
        nombre_album=request.GET["nombre_album"]
        albums=Album.objects.filter(nombre_album__icontains=nombre_album)
        return render(request, "AppCoder/resultados_busqueda_album.html", {"albums":albums})
    else:
        return render(request, "AppCoder/busqueda_album.html", {"error": "No se ingresó ningún album con ese nombre"})
