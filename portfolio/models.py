from django.db import models

# Create your models here.

class Project(models.Model):

    title= models.CharField(max_length=200, verbose_name="Titulo")
    description= models.TextField(verbose_name="Descripción")
    image= models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)
    # se añade la hora en que se creo el archivo
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    #se añade la hora en la que fue modificado o se actuliza  el el archivo
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")



    class Meta: 

        verbose_name= "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title    








