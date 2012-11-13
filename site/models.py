from django.db import models

# Create your models here.

class User(models.Model):
	name                = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.name

class Tape(models.Model):
	submitter   		= models.ForeignKey(User)
	title               = models.CharField(max_length=255)
	author              = models.CharField(max_length=255)
	year                = models.DateField()
	location    		= models.CharField(max_length=255)
	image_url   		= models.CharField(max_length=255, blank=True)
	history             = models.TextField()
	
	def __unicode__(self):
		return self.title

class Side(models.Model):
	tape                = models.ForeignKey(Tape)
	side                = models.CharField(max_length=1)
	image_url   		= models.CharField(max_length=255)
	music_url   		= models.CharField(max_length=255)

	def __unicode__(self):
		return self.tape.title + ' - ' + self.side

class Track(models.Model):
	side                = models.ForeignKey(Side)
	song_title  		= models.CharField(max_length=255)
	artist              = models.CharField(max_length=255)
	track_num   		= models.IntegerField()

	def __unicode__(self):
		return self.artist

class Artwork(models.Model):
	tape                = models.ForeignKey(Tape)
	side                = models.ForeignKey(Side)
	image_url           = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.image_url


