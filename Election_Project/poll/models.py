import datetime
from urllib import request
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth.models import User


class Poll(models.Model):
      question = models.TextField()
      #candidate_one = models.CharField(max_length=30)
      #candidate = models.CharField(max_length=30,default=0)
      #candidate_two = models.CharField(max_length=30,default=0)
      #candidate_three = models.CharField(max_length=30,default=0)
      #candidate_one_count = models.IntegerField(default=0)
      #candidate_count = models.IntegerField(default=0)
      #candidate_two_count = models.IntegerField(default=0)
      #candidate_three_count = models.IntegerField(default=0)
      candidate = models.CharField(max_length=30,default=0)
      candidate_count = models.IntegerField(default=0)
      pub_date = models.DateTimeField('date published',default=timezone.now)
      close_date = models.DateTimeField('date close',default=timezone.now)
      def __str__(self):
        return self.question
      @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?', 
        )
      def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
      @property
      def is_active(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.close_date <= now
      def total(self):
        return  self.candidate_count
    
      
class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    description_text = models.CharField(max_length=2000,default="")
    #candidate_image = models.ImageField(upload_to='static/images', null=True,blank=True,default="")
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    

    def __str__(self):
        return self.choice_text
   