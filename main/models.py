from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.TextField(max_length=300)
    def __unicode__(self):
        return self.name
class Topic(models.Model):
    name = models.TextField(max_length=300)
    def __unicode__(self):
        return self.name
class Question(models.Model):
    name = models.TextField(max_length=1000)
    topic_name = models.ForeignKey(Topic)
    SCORE_CHOICES = (
        (10, 10),
        (20, 20),
        (30, 30),
        (40, 40),
        (50, 50)
    )
    score = models.IntegerField(choices=SCORE_CHOICES)
    image = models.ImageField(blank=True, null=True, upload_to='imgs/questions')
    used = models.BooleanField(default=False)
    team_answered = models.ForeignKey(Team, blank=True, null=True)
    question_answer = models.TextField(max_length=1000)
    answer_image = models.ImageField(blank=True, null=True, upload_to='imgs/answers')


    def __unicode__(self):
        return self.topic_name.name + ": " + self.name

    class Meta:
        unique_together = ('topic_name', 'score')

