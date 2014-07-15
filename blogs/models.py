from django.db import models
from mptt.models import MPTTModel, TreeForeignKey  

from django.db import models
import datetime  

class Post(models.Model): 
	""" Blog entry """ 
	title = models.CharField(max_length=255) 
	text = models.TextField() 
	added = models.DateTimeField(default=datetime.datetime.now)

	def __unicode__(self):
		return str(self.title)

class Comment(MPTTModel): 
	""" Threaded comments for blog posts """ 
	post = models.ForeignKey(Post) 
	author = models.CharField(max_length=60) 
	comment = models.TextField() 
	added = models.DateTimeField(default=datetime.datetime.now) 
	# a link to comment that is being replied, if one exists 
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children')  

	def __unicode__(self):
		return str(self.comment[:100])

	class MPTTMeta: 
		# comments on one level will be ordered by date of creation 
		order_insertion_by=['added']