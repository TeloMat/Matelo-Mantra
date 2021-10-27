from django.db import models
from django.contrib.auth.models import User

from main.posts.forms import CreateNewPost, EditPost, AddPostCredit


class Post(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(max_length=800, blank=True)
    thumbnail = models.ImageField(upload_to='posts/thumbnails', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return "Title: " + self.name

    def handle_files(self, cleaned_data):
        if cleaned_data.get('thumbnail'):
            self.thumbnail.save(self.name + "_thumbnail.jpg", cleaned_data.get('thumbnail'))

    def handle_data(self, cleaned_data):
        self.name = cleaned_data.get('name')
        if cleaned_data.get('text'):
            self.text = cleaned_data.get('text')
        self.public = cleaned_data.get('public')
        self.handle_files(cleaned_data)
        self.save()

    def create_post(self, response, **kwargs):
        form = CreateNewPost(response.POST, response.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            self.handle_data(cleaned_data)
            return True
        return False

    def edit_post(self, response, **kwargs):
        form = EditPost(self, response.POST, response.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            self.handle_data(cleaned_data)
            return True
        return False

    def delete_post(self):
        self.thumbnail.delete()
        for credit in self.credits:
            credit.delete_credit()
        self.delete()

    def add_credit(self, response):
        form = AddPostCredit(response.POST, response.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            self.credits.create(
                contributor=cleaned_data.get('contributor'),
                contribution=response.FILES.get('contribution')
            )
            return True
        return False

    def get_credits(self):
        if not self.public:
            return None
        return PostCredit.objects.filter(self.id)


class PostCredit(models.Model):
    post = models.ForeignKey(Post, related_name='credits', on_delete=models.CASCADE, null=True)
    contributor = models.CharField(max_length=50)
    contribution = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.contributor + ": " + self.contribution

    def delete_credit(self):
        self.delete()
