from django.db import models
from django.utils import timezone


class Poll(models.Model):
      question = models.TextField()
      candidate_one = models.CharField(max_length=30)
      candidate_two = models.CharField(max_length=30)
      candidate_three = models.CharField(max_length=30)
      candidate_one_count = models.IntegerField(default=0)
      candidate_two_count = models.IntegerField(default=0)
      candidate_three_count = models.IntegerField(default=0)
      pub_date = models.DateTimeField('date published',default=timezone.now)
      close_date = models.DateTimeField('date close',default=timezone.now)
      def __str__(self):
        return self.question
      def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
      @property
      def is_active(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.close_date <= now
      def total(self):
        return self.candidate_one_count + self.candidate_two_count + self.candidate_three_count
class Choice(models.Model):
    question = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    description_text = models.CharField(max_length=2000,default="")
    candidate_image = models.ImageField(upload_to='Images',default="")
    def __str__(self):
        return self.choice_text