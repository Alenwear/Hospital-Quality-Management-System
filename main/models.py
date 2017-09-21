from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class AgentInfo(models.Model):
    AgentInfo_id = models.IntegerField(default=0)
    AgentInfo_id.primary_key = True
    opId = models.IntegerField
    dt = models.DateTimeField("date published")
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=5)
    memCode = models.CharField(max_length=5)
    isOnUse = models.BooleanField(default=False)
    isOp = models.BooleanField(default=False)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class AdmInfo(models.Model):
    AdmInfo_id = models.IntegerField(default=0)
    AdmInfo_id.primary_key = True
    fk_AdmInfo_opId = models.ForeignKey(AgentInfo, related_name='AdmInfo_opId', on_delete=models.CASCADE)
    dt = models.DateTimeField('date published')
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=4)
    memCode = models.CharField(max_length=15)
    prCode = models.IntegerField(default=0)
    isAdmEr = models.BooleanField(default=False)
    isAdmEe = models.BooleanField(default=False)
    isOnUse = models.BooleanField(default=False)
    isDeleted = models.BooleanField(default=False)
    isCmted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class CheInfo(models.Model):
    CheInfo_id = models.IntegerField(default=0)
    CheInfo_id.primary_key = True
    fk_CheInfo_opId = models.ForeignKey(AgentInfo, related_name='CheInfo_opId', on_delete=models.CASCADE)
    fk_CheInfo_admErId = models.ForeignKey(AdmInfo, related_name='CheInfo_admErId', on_delete=models.CASCADE)
    fk_CheInfo_admEeId = models.ForeignKey(AdmInfo, related_name='CheInfo_admEeId', on_delete=models.CASCADE)
    dt = models.DateTimeField("date published")
    time = models.DateField("date published")
    type = models.CharField(max_length=50)
    manageScore = models.IntegerField(default=0)
    personScore = models.IntegerField(default=0)
    fee = models.IntegerField(default=0)
    reason = models.TextField()

    def __str__(self):
        return str(self.dt)
