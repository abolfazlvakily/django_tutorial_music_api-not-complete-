from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    nickname = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return '{}_{}'.format(self.first_name, self.last_name)
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        elif self.nickname:
            return self.nickname

    # حتما باید یکی از فیلد ها پر باشد تا عملیات ذخیره سازی صورت پذیرد
    def save(self, *args, **kwargs):
        if self.nickname or self.last_name or self.first_name:
            super().save(*args, **kwargs)


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20, null=True, blank=False)
    summary = models.CharField(null=True, blank=True, max_length=255)
    discriotion = models.TextField(null=True, blank=True)
    cover = models.ImageField(null=True, blank=True, upload_to='photo/Album/%Y/%m/%d/')
    rate = models.FloatField(null=True, blank=True)
    like = models.PositiveSmallIntegerField(null=True, default=0, blank=True)
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    title = models.CharField(null=True, blank=True, max_length=20)

    def __str__(self):
        return self.title


class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    title = models.CharField(null=True, max_length=20, blank=True)
    music = models.FileField(null=True, upload_to='music/Track/%Y/%m/%d/')


    def __str__(self):
        return self.title
