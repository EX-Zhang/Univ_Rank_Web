# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class UnivRank(models.Model):
    univ_id = models.IntegerField(db_column='Univ_ID', primary_key=True)  # Field name made lowercase.
    univ_rank = models.CharField(db_column='Univ_Rank', max_length=255, blank=True, null=True)  # Field name made lowercase.
    univ_name = models.CharField(db_column='Univ_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    univ_reign = models.CharField(db_column='Univ_Reign', max_length=255, blank=True, null=True)  # Field name made lowercase.
    univ_score = models.CharField(db_column='Univ_Score', max_length=255, blank=True, null=True)  # Field name made lowercase.
    univ_stud_rate = models.CharField(db_column='Univ_Stud_Rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    univ_prof_rate = models.CharField(db_column='Univ_Prof_Rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    univ_prof_stud_rate = models.CharField(db_column='Univ_Prof_Stud_Rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    univ_ref_rate = models.CharField(db_column='Univ_Ref_Rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    univ_acad_repu = models.CharField(db_column='Univ_Acad_Repu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    univ_employer_repu = models.CharField(db_column='Univ_Employer_Repu', max_length=255, blank=True, null=True)  # Field name made lowercase.
    univ_reign_en = models.CharField(db_column='Univ_Reign_EN', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'univ_rank'
