from django.db import models

LANGS = (
			('C','C'),
			('C++','C++'),
			('Java','Java'),
			('python','python')
		)


	
class Submissions(models.Model):
    rid = models.IntegerField(db_index=True,primary_key=True)
    pid = models.IntegerField(blank=True, null=True)
    tid = models.IntegerField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    access = models.TextField(blank=True, null=True)
    submittime = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    output = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'submissions'
        verbose_name_plural = 'submissions'


# class Runs(models.Model):
#     rid = models.IntegerField(db_index=True,primary_key=True)
#     pid = models.IntegerField(blank=True, null=True)
#     tid = models.IntegerField(blank=True, null=True)
#     language = models.TextField(blank=True, null=True)
#     time = models.TextField(blank=True, null=True)
#     result = models.TextField(blank=True, null=True)
#     access = models.TextField(blank=True, null=True)
#     submittime = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'runs'
#         verbose_name_plural = 'runs'
