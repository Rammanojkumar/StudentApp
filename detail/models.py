from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Rank(models.Model):
    rankId = models.AutoField(primary_key=True)
    Desc = models.CharField(max_length=60)

    def __str__(self):
        return '%s - %s' % (self.rankId, self.Desc)

class CourseDetails(models.Model):
    courseId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=60)

    def __str__(self):
        return '%s - %s' % (self.courseId, self.courseName)

class Student(models.Model):
    studentId = models.AutoField(primary_key=True)
    studentName = models.CharField(max_length=60)
    CourseID= models.ForeignKey(CourseDetails, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '%s - %s' % (self.studentId, self.studentName)




class StudentDetail(models.Model):
    id = models.AutoField(primary_key=True)
    studentId= models.ForeignKey(Student, on_delete=models.CASCADE)
    rankId = models.ForeignKey(Rank, on_delete=models.CASCADE)
    Score= models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return '%s %s' % (self.studentId, self.Score)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




