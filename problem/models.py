from django.db import models
#from settings import .
# from account.models import User


# class AbstractProblem(models.Model):

#     class Meta:
#         abstract = True


# class Problem(AbstractProblem):
#     pass


# class Solution(models.Model):
#     user = models.ForeignKey(User)
#     problem = models.ForeignKey(Problem)

# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)

LANGS = (
			('C','C'),
			('C++','C++'),
			('Java','Java'),
			('python','python')
		)

IO = (
		('Y','yes'),
		('N','no')
	)
STATUS = (
		('Y','yes'),
		('N','no')
	)
CONTEST = (
		('Prac','Practice'),
		('Rated','Rated')
	)


class Problems(models.Model):
    pid = models.IntegerField(primary_key=True,db_index=True)
    code = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    pro_type = models.TextField(blank=True, null=True)
    contest = models.TextField()
    status = models.TextField(blank=True, null=True)
    pgroup = models.TextField(blank=True, null=True)
    statement = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    imgext = models.TextField(blank=True, null=True)
    pro_input = models.TextField(blank=True, null=True)
    pro_output = models.TextField(blank=True, null=True)
    timelimit = models.FloatField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)
    displayio = models.IntegerField()
    maxfilesize = models.IntegerField()
    solved = models.IntegerField()
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'problems'
        verbose_name_plural = 'problems'
