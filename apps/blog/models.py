import uuid

from django.db import models
from django.utils import timezone
from django.utils.text import slugify



def blog_thumbnail_directory(instance, filename):
    return f'blog/{instance.title}/{filename}'
    # return "blog/{0}/{1}".format(instance.title, filename)

def category_thumbnail_directory(instance, filename):
    return f'blog_categories/{instance.name}/{filename}'
    # return "category/{0}/{1}".format(instance.name, filename)


class Category(models.Model): #categorias dinamicas
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to=category_thumbnail_directory)
    slug = models.CharField(max_length=128)

    def __str__(self):
        return self.name


# Create your models here.
class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    status_options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to=blog_thumbnail_directory)

    keywords = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=15, choices=status_options, default='draft')

    objects = models.Manager() # The default manager
    postobjects = PostObjects() # The custom manager

    class Meta:
        ordering = ('status', '-created_at')

    def __str__(self):
        return self.title
    

class Headding(models.Model):
    # asasas

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='headdings')
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    level = models.IntegerField(
        choices=(
            (1, 'H1'),
            (2, 'H2'),
            (3, 'H3'),
            (4, 'H4'),
            (5, 'H5'),
            (6, 'H6'),
        )
    )
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) # para eliminar los espacios dentro de las palabras
        super().save(args, **kwargs)





