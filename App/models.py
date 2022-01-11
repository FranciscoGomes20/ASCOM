from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Urgency(models.Model):
    description = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.description

class Sector(models.Model):
    sector = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.sector
    
class Requestion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    anexo = models.ImageField('Imagem', upload_to='App\img_upload', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, blank=True, null=True)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='applicant', on_delete=models.CASCADE, blank=True, null=True)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='assigned', on_delete=models.CASCADE, blank=True, null=True)
    urgency = models.ForeignKey(Urgency, on_delete=models.CASCADE, blank=True, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    final_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
