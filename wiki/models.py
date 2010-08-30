from django.db import models

from templatetags.wiki import wikify


class Page(models.Model):
    name = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    rendered = models.TextField()

    class Meta:
        ordering = ('name', )

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = self.name
        self.rendered = wikify(self.content)
        super(Page, self).save(*args, **kwargs)
