from django.db import models

# Create your models here.
class Playlist(models.Model):
    nombre_cancion= models.CharField(max_length=50)

    artista= models.CharField(max_length=50)

    album= models.CharField(max_length=50) 

    def __str__(self):
        return self.nombre_cancion+" - "+str(self.artista)


class Artista(models.Model):
    nombre_completo= models.CharField(max_length=50)

    nacionalidad= models.CharField(max_length=50)

    arte= models.CharField(max_length=50) 

    def __str__(self):
        return self.nombre_completo+" - "+str(self.arte)


class Album(models.Model):
    nombre_album= models.CharField(max_length=50)

    creador= models.CharField(max_length=50)

    año= models.IntegerField()

    def __str__(self):
        return self.nombre_album+ " by "+self.creador +" - "+str(self.año)
