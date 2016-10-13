from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

def upload_location(instance,filename):
    return "%s/%s" %(instance.user,filename)
class post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title=models.CharField(max_length=140)
    image=models.ImageField(null=True,blank=True,width_field="width",height_field="height")
    height=models.IntegerField(default=640)
    width=models.IntegerField(default=640)
    content=models.TextField()
    last_seen=models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)

    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("detail",kwargs={"var":self.id})
        # return "/news/%s" %(self.id)
    class Meta:
        ordering=["-timestamp","-last_seen"]
# Create your models here.
