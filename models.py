from django.db import models

class Membresia(models.Model): # Primero Membresia, porque Miembro hace referencia a ella
    id_membresia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, help_text="Nombre de la membresía (ej. Bronce, Plata, Oro)")
    descripcion = models.TextField()
    costo_mensual = models.DecimalField(max_digits=6, decimal_places=2)
    acceso_limitado = models.BooleanField(default=False, help_text="¿Esta membresía tiene acceso limitado a ciertas áreas o clases?")
    acceso_entrenador = models.BooleanField(default=False, help_text="¿Incluye acceso a entrenador personal?")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Membresía"
        verbose_name_plural = "Membresías"

class Miembro(models.Model):
    id_miembro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    id_membresia = models.ForeignKey(Membresia, on_delete=models.SET_NULL, related_name='miembros_con_esta_membresia', blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='img_miembros/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"