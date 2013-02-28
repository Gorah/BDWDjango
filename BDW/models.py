# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class ThrJobdetails(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.ForeignKey(ThrEmployee, null=True, db_column='EEID', blank=True) # Field name made lowercase.
    project = models.ForeignKey(ThrMru, null=True, db_column='Project', blank=True) # Field name made lowercase.
    workcontracttype = models.ForeignKey(ThrContracttype, null=True, db_column='WorkContractType', blank=True) # Field name made lowercase.
    costcenter = models.TextField(db_column='CostCenter', blank=True) # Field name made lowercase.
    jobcode = models.TextField(db_column='JobCode', blank=True) # Field name made lowercase.
    jobtitle = models.TextField(db_column='JobTitle', blank=True) # Field name made lowercase.
    eelevel = models.ForeignKey(ThrEmployeelevel, null=True, db_column='EELevel', blank=True) # Field name made lowercase.
    fte = models.FloatField(null=True, db_column='FTE', blank=True) # Field name made lowercase.
    fullparttime = models.ForeignKey(ThrFullparttime, null=True, db_column='FullPartTime', blank=True) # Field name made lowercase.
    provider = models.ForeignKey(ThrContractorprovider, null=True, db_column='Provider', blank=True) # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True) # Field name made lowercase.
    startdate = models.CharField(max_length=10, db_column='StartDate') # Field name made lowercase.
    enddate = models.CharField(max_length=10, db_column='EndDate') # Field name made lowercase.
    modifieddate = models.CharField(max_length=10, db_column='ModifiedDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_JobDetails'

class InnoStages(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    project = models.ForeignKey(InnoProjects, null=True, db_column='Project_id', blank=True) # Field name made lowercase.
    stagetype = models.ForeignKey(InnoStagestypes, null=True, db_column='StageType_id', blank=True) # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True) # Field name made lowercase. This field type is a guess.
    commiter = models.IntegerField(null=True, db_column='Commiter', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Inno_Stages'

class ThrSeattype(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    seattype = models.TextField(primary_key=True, db_column='SeatType') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_SeatType'

class InnoCertificates(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    cert_type = models.IntegerField(null=True, db_column='Cert_type', blank=True) # Field name made lowercase.
    eeid = models.IntegerField(null=True, db_column='EEID', blank=True) # Field name made lowercase.
    dateofgrant = models.TextField(db_column='DateOfGrant', blank=True) # Field name made lowercase. This field type is a guess.
    granter = models.IntegerField(null=True, db_column='Granter', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Inno_Certificates'

class TkmProgramtype(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    programname = models.TextField(db_column='ProgramName') # Field name made lowercase.
    progdescription = models.TextField(db_column='ProgDescription', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tKM_ProgramType'

class ThrScorecardmetrics(models.Model):
    metric_name = models.CharField(max_length=120, db_column='Metric Name') # Field renamed to remove spaces. Field name made lowercase.
    description = models.CharField(max_length=250, db_column='Description', blank=True) # Field name made lowercase.
    target = models.CharField(max_length=20, db_column='Target', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_ScorecardMetrics'

class InnoCertificatestypes(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    nameofcertificate = models.TextField(db_column='NameOfCertificate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Inno_CertificatesTypes'

class ThrSeatgroup(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    seatgroup = models.TextField(primary_key=True, db_column='SeatGroup') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_SeatGroup'

class ThrSeats(models.Model):
    seatid = models.IntegerField(primary_key=True, db_column='SeatID') # Field name made lowercase.
    building = models.TextField(db_column='Building') # Field name made lowercase.
    buildingfloor = models.IntegerField(db_column='BuildingFloor') # Field name made lowercase.
    seattype = models.ForeignKey(ThrSeattype, null=True, db_column='SeatType', blank=True) # Field name made lowercase.
    mrucode = models.ForeignKey(ThrMru, null=True, db_column='MRUCode', blank=True) # Field name made lowercase.
    eeid = models.ForeignKey(ThrEmployee, null=True, db_column='EEID', blank=True) # Field name made lowercase.
    groupid = models.ForeignKey(ThrSeatgroup, null=True, db_column='GroupID', blank=True) # Field name made lowercase.
    securearea = models.BooleanField(db_column='SecureArea') # Field name made lowercase.
    eetype = models.ForeignKey(ThrSeateetype, null=True, db_column='EEType', blank=True) # Field name made lowercase.
    stardate = models.CharField(max_length=10, db_column='StarDate') # Field name made lowercase.
    enddate = models.CharField(max_length=10, db_column='EndDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_Seats'

class ThrSeateetype(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    eetype = models.TextField(primary_key=True, db_column='EEType') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_SeatEEType'

class TdashSubprocesses(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    subprocessname = models.TextField(db_column='SubProcessName') # Field name made lowercase.
    subprocessdefinition = models.TextField(db_column='SubProcessDefinition', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tDash_SubProcesses'

class InnoSavingtype(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    savingname = models.TextField(db_column='SavingName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Inno_SavingType'

class TkmInternaltrainers(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.ForeignKey(ThrEmployee, db_column='EEID') # Field name made lowercase.
    nominationdate = models.CharField(max_length=10, db_column='NominationDate') # Field name made lowercase.
    creditgranted = models.FloatField(null=True, db_column='CreditGranted', blank=True) # Field name made lowercase.
    creditaccumulated = models.FloatField(null=True, db_column='CreditAccumulated', blank=True) # Field name made lowercase.
    creditused = models.FloatField(null=True, db_column='CreditUsed', blank=True) # Field name made lowercase.
    creditbalance = models.FloatField(null=True, db_column='CreditBalance', blank=True) # Field name made lowercase.
    certified = models.BooleanField(null=True, db_column='Certified', blank=True) # Field name made lowercase.
    itsdone = models.BooleanField(null=True, db_column='ITSDone', blank=True) # Field name made lowercase.
    traininghours_granted = models.FloatField(null=True, db_column='TrainingHours_granted', blank=True) # Field name made lowercase.
    traininghours = models.FloatField(null=True, db_column='TrainingHours', blank=True) # Field name made lowercase.
    traininghours_balance = models.FloatField(null=True, db_column='TrainingHours_balance', blank=True) # Field name made lowercase.
    deptinttrainer = models.BooleanField(null=True, db_column='DeptIntTrainer', blank=True) # Field name made lowercase.
    creditspendon = models.TextField(db_column='CreditSpendOn', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'tKM_InternalTrainers'

class TkmSvlimits(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    svid = models.ForeignKey(ThrEmployee, null=True, db_column='SVID', blank=True) # Field name made lowercase.
    limit = models.SmallIntegerField(null=True, db_column='Limit', blank=True) # Field name made lowercase.
    validitydate = models.CharField(max_length=10, db_column='ValidityDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tKM_SVLimits'

class ThrTeammembers(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    teamname = models.ForeignKey(ThrTeamlist, null=True, db_column='TeamName', blank=True) # Field name made lowercase.
    eeid = models.ForeignKey(ThrEmployee, null=True, db_column='EEID', blank=True) # Field name made lowercase.
    startdate = models.CharField(max_length=10, db_column='StartDate') # Field name made lowercase.
    enddate = models.CharField(max_length=10, db_column='EndDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_TeamMembers'

class TkmEnrollmentspoc(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    spocid = models.ForeignKey(ThrEmployee, null=True, db_column='SpocID', blank=True) # Field name made lowercase.
    svid = models.ForeignKey(ThrEmployee, null=True, db_column='SVID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tKM_EnrollmentSPOC'

class TdashTower(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    towername = models.TextField(db_column='TowerName') # Field name made lowercase.
    class Meta:
        db_table = u'tDash_Tower'

class ThrAbsence(models.Model):
    eeid = models.IntegerField(db_column='EEID') # Field name made lowercase.
    absencetype = models.TextField(db_column='AbsenceType', blank=True) # Field name made lowercase.
    absencedate = models.CharField(max_length=10, db_column='AbsenceDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_Absence'

class ThrActiontype(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    actiontype = models.TextField(primary_key=True, db_column='ActionType') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_ActionType'

class TkmTrainingneeds(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    svid = models.ForeignKey(ThrEmployee, null=True, db_column='SVID', blank=True) # Field name made lowercase.
    trainigid = models.ForeignKey(TkmTrainingmasterlist, null=True, db_column='TrainigID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tKM_TrainingNeeds'

class TdashProcesses(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    processname = models.TextField(db_column='ProcessName') # Field name made lowercase.
    towerid = models.ForeignKey(TdashTower, db_column='TowerID') # Field name made lowercase.
    subprocessdefinition = models.TextField(db_column='SubProcessDefinition', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tDash_Processes'

class ThrActionreason(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    reasoncode = models.TextField(primary_key=True, db_column='ReasonCode') # Field name made lowercase.
    parentaction = models.IntegerField(null=True, db_column='ParentAction', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_ActionReason'

class InnoProjects(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    projecttitle = models.TextField(db_column='ProjectTitle', blank=True) # Field name made lowercase.
    client = models.ForeignKey(InnoClients, null=True, db_column='Client_id', blank=True) # Field name made lowercase.
    projecttype = models.ForeignKey(InnoProjecttypes, null=True, db_column='ProjectType_id', blank=True) # Field name made lowercase.
    processtower_id = models.IntegerField(null=True, db_column='ProcessTower_id', blank=True) # Field name made lowercase.
    objective = models.ForeignKey(InnoObjectives, null=True, db_column='Objective_id', blank=True) # Field name made lowercase.
    qualityleader = models.ForeignKey(InnoQualityleads, null=True, db_column='QualityLeader_id', blank=True) # Field name made lowercase.
    projectlead_id = models.IntegerField(null=True, db_column='ProjectLead_id', blank=True) # Field name made lowercase.
    projectmentor_id = models.IntegerField(null=True, db_column='ProjectMentor_id', blank=True) # Field name made lowercase.
    projectlead = models.TextField(db_column='ProjectLead', blank=True) # Field name made lowercase.
    startdate = models.CharField(max_length=10, db_column='StartDate', blank=True) # Field name made lowercase.
    completiondate = models.CharField(max_length=10, db_column='CompletionDate', blank=True) # Field name made lowercase.
    savingtype = models.IntegerField(null=True, db_column='SavingType', blank=True) # Field name made lowercase.
    hpsavings = models.FloatField(null=True, db_column='HPSavings', blank=True) # Field name made lowercase.
    projectowner = models.IntegerField(null=True, db_column='ProjectOwner', blank=True) # Field name made lowercase.
    approval = models.BooleanField(null=True, db_column='Approval', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Inno_Projects'

class TdashSubprocessassigment(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    subproc = models.ForeignKey(TdashSubprocesses, null=True, db_column='SubProc', blank=True) # Field name made lowercase.
    process = models.ForeignKey(TdashProcesses, null=True, db_column='Process', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tDash_SubProcessAssigment'

class ThrActions(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.ForeignKey(ThrEmployee, db_column='EEID') # Field name made lowercase.
    actiontype = models.ForeignKey(ThrActiontype, db_column='ActionType') # Field name made lowercase.
    reasoncode = models.ForeignKey(ThrActionreason, db_column='ReasonCode') # Field name made lowercase.
    stardate = models.CharField(max_length=10, db_column='StarDate') # Field name made lowercase.
    enddate = models.CharField(max_length=10, db_column='EndDate') # Field name made lowercase.
    modifieddate = models.TextField(db_column='ModifiedDate') # Field name made lowercase. This field type is a guess.
    modifiedby = models.TextField(db_column='ModifiedBy') # Field name made lowercase.
    employmentstatus = models.TextField(db_column='EmploymentStatus', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_Actions'

class Test(models.Model):
    a = models.TextField(blank=True)
    b = models.TextField(blank=True)
    class Meta:
        db_table = u'test'

class TkmTraininglist(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    trainingid = models.ForeignKey(TkmTrainingmasterlist, null=True, db_column='TrainingID', blank=True) # Field name made lowercase.
    startdate = models.CharField(max_length=10, db_column='StartDate', blank=True) # Field name made lowercase.
    enddate = models.CharField(max_length=10, db_column='EndDate', blank=True) # Field name made lowercase.
    enrolstart = models.TextField(db_column='EnrolStart', blank=True) # Field name made lowercase. This field type is a guess.
    enrolend = models.TextField(db_column='EnrolEnd', blank=True) # Field name made lowercase. This field type is a guess.
    numberofseats = models.SmallIntegerField(null=True, db_column='NumberOfSeats', blank=True) # Field name made lowercase.
    hours = models.SmallIntegerField(null=True, db_column='Hours', blank=True) # Field name made lowercase.
    loyalityagreement = models.BooleanField(null=True, db_column='LoyalityAgreement', blank=True) # Field name made lowercase.
    trlanguage = models.TextField(db_column='TrLanguage', blank=True) # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True) # Field name made lowercase.
    trainingroom = models.TextField(db_column='TrainingRoom', blank=True) # Field name made lowercase.
    enrolllock = models.BooleanField(null=True, db_column='EnrollLock', blank=True) # Field name made lowercase.
    teamlock = models.BooleanField(null=True, db_column='TeamLock', blank=True) # Field name made lowercase.
    importantinfo = models.TextField(db_column='ImportantInfo', blank=True) # Field name made lowercase. This field type is a guess.
    trainer1 = models.ForeignKey(TkmInternaltrainers, null=True, db_column='Trainer1', blank=True) # Field name made lowercase.
    trainer2 = models.ForeignKey(TkmInternaltrainers, null=True, db_column='Trainer2', blank=True) # Field name made lowercase.
    mru_limit = models.TextField(db_column='MRU_Limit', blank=True) # Field name made lowercase.
    tr_owner = models.CharField(max_length=35, db_column='Tr_Owner', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tKM_TrainingList'

class InnoClients(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    clientname = models.TextField(db_column='ClientName', blank=True) # Field name made lowercase. This field type is a guess.
    parentmru = models.TextField(db_column='ParentMRU', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'Inno_Clients'

class ThrTower(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    towername = models.TextField(primary_key=True, db_column='TowerName') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_Tower'

class InnoComments(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    projectid = models.ForeignKey(InnoProjects, null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    commenter_eeid = models.ForeignKey(ThrEmployee, null=True, db_column='Commenter_eeid', blank=True) # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase. This field type is a guess.
    date = models.TextField(db_column='Date', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'Inno_Comments'

class InnoObjectives(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    objectivename = models.TextField(db_column='ObjectiveName', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'Inno_Objectives'

class TieTower(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    ietowernamename = models.TextField(primary_key=True, db_column='IETowerNameName') # Field name made lowercase.
    class Meta:
        db_table = u'tIE_Tower'

class InnoProcesstowers(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    towername = models.TextField(db_column='TowerName', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'Inno_ProcessTowers'

class ThrMru(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    mru = models.TextField(primary_key=True, db_column='MRU') # Field name made lowercase.
    ownerid = models.IntegerField(null=True, db_column='OwnerID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_MRU'

class ThrLanguagesserved(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    language = models.TextField(db_column='Language', blank=True) # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True) # Field name made lowercase.
    teamname = models.ForeignKey(ThrTeamlist, null=True, db_column='TeamName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_LanguagesServed'

class ThrInmig(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_InMIG'

class ThrBuildinglist(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    buildingname = models.TextField(db_column='BuildingName', blank=True) # Field name made lowercase.
    buildingid = models.TextField(db_column='BuildingID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_BuildingList'

class ThrEmployeelevel(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    emplevel = models.TextField(primary_key=True, db_column='EmpLevel') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_EmployeeLevel'

class InnoProjecttypes(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    typename = models.TextField(db_column='TypeName', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'Inno_ProjectTypes'

class ThrBuildingdetails(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    buildingname = models.TextField(db_column='BuildingName', blank=True) # Field name made lowercase.
    buildingid = models.TextField(db_column='BuildingID', blank=True) # Field name made lowercase.
    floorno = models.SmallIntegerField(null=True, db_column='FloorNo', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_BuildingDetails'

class Tcompgs(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    date = models.TextField(db_column='Date') # Field name made lowercase.
    green = models.SmallIntegerField(null=True, db_column='Green', blank=True) # Field name made lowercase.
    red = models.SmallIntegerField(null=True, db_column='Red', blank=True) # Field name made lowercase.
    mru = models.TextField(db_column='MRU') # Field name made lowercase.
    group = models.TextField(db_column='Group') # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase.
    user = models.TextField(db_column='User', blank=True) # Field name made lowercase.
    changes = models.TextField(db_column='Changes', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tCompGS'

class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, unique=True)
    principal_id = models.IntegerField(unique=True)
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(null=True, blank=True)
    definition = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = u'sysdiagrams'

class InnoQualityleads(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.ForeignKey(ThrEmployee, null=True, db_column='EEID', blank=True) # Field name made lowercase.
    nominationdate = models.TextField(db_column='NominationDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Inno_QualityLeads'

class ThrInternalfunction(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    intfunction = models.TextField(primary_key=True, db_column='IntFunction') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_InternalFunction'

class OpsEscalationsActionfiles(models.Model):
    id = models.ForeignKey(OpsEscalationsDetails, null=True, db_column='ID', blank=True) # Field name made lowercase.
    fileid = models.AutoField(primary_key=True, db_column='fileID') # Field name made lowercase.
    path = models.CharField(max_length=250, blank=True)
    uploadedby = models.CharField(max_length=250, db_column='uploadedBy', blank=True) # Field name made lowercase.
    uploadedon = models.TextField(db_column='uploadedOn', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'Ops_Escalations_ActionFiles'

class OpsEscalationsLog(models.Model):
    id = models.ForeignKey(OpsEscalationsDetails, null=True, db_column='ID', blank=True) # Field name made lowercase.
    logid = models.AutoField(primary_key=True, db_column='logID') # Field name made lowercase.
    loggedbyid = models.IntegerField(null=True, db_column='loggedById', blank=True) # Field name made lowercase.
    loggedbyname = models.CharField(max_length=80, db_column='loggedByName', blank=True) # Field name made lowercase.
    loggedon = models.TextField(db_column='loggedOn', blank=True) # Field name made lowercase. This field type is a guess.
    comment = models.TextField(db_column='Comment', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Ops_Escalations_Log'

class InnoStagestypes(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    stagename = models.TextField(db_column='StageName', blank=True) # Field name made lowercase. This field type is a guess.
    projecttype = models.ForeignKey(InnoProjecttypes, null=True, db_column='ProjectType_id', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Inno_StagesTypes'

class TkmLoyalityagree(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.ForeignKey(ThrEmployee, null=True, db_column='EEID', blank=True) # Field name made lowercase.
    loyalitytype = models.IntegerField(null=True, db_column='LoyalityType', blank=True) # Field name made lowercase.
    signedon = models.CharField(max_length=10, db_column='SignedON', blank=True) # Field name made lowercase.
    loyalitystarts = models.CharField(max_length=10, db_column='LoyalityStarts', blank=True) # Field name made lowercase.
    la_startvalue = models.IntegerField(null=True, db_column='LA_startValue', blank=True) # Field name made lowercase.
    lalength = models.IntegerField(null=True, db_column='LALength', blank=True) # Field name made lowercase.
    payback = models.DecimalField(decimal_places=4, null=True, max_digits=10, db_column='PayBack', blank=True) # Field name made lowercase.
    loyalityends = models.CharField(max_length=10, db_column='LoyalityEnds', blank=True) # Field name made lowercase.
    la_creator = models.IntegerField(null=True, db_column='LA_Creator', blank=True) # Field name made lowercase.
    la_createdon = models.TextField(db_column='LA_CreatedOn', blank=True) # Field name made lowercase. This field type is a guess.
    la_changer = models.IntegerField(null=True, db_column='LA_Changer', blank=True) # Field name made lowercase.
    la_changedate = models.TextField(db_column='LA_ChangeDate', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'tKM_LoyalityAgree'

class TuserMasterlist(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    username = models.TextField(primary_key=True, db_column='UserName') # Field name made lowercase.
    ntid = models.TextField(unique=True, db_column='NTID') # Field name made lowercase.
    userexpiration = models.CharField(max_length=10, db_column='UserExpiration') # Field name made lowercase.
    userpassword = models.TextField(db_column='UserPassword') # Field name made lowercase.
    class Meta:
        db_table = u'tUser_MasterList'

class TkmLoyalitytypes(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    loyalityname = models.CharField(max_length=50, db_column='LoyalityName') # Field name made lowercase.
    loyality_ammount = models.IntegerField(db_column='Loyality_Ammount') # Field name made lowercase.
    class Meta:
        db_table = u'tKM_LoyalityTypes'

class TkmEnrolmentList(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.ForeignKey(ThrEmployee, null=True, db_column='EEID', blank=True) # Field name made lowercase.
    enroldate = models.CharField(max_length=10, db_column='EnrolDate', blank=True) # Field name made lowercase.
    trainingid = models.ForeignKey(TkmTraininglist, null=True, db_column='TrainingID', blank=True) # Field name made lowercase.
    accepted = models.BooleanField(null=True, db_column='Accepted', blank=True) # Field name made lowercase.
    listedtime = models.TextField(db_column='ListedTime', blank=True) # Field name made lowercase. This field type is a guess.
    attended = models.BooleanField(null=True, db_column='Attended', blank=True) # Field name made lowercase.
    reservespot = models.BooleanField(null=True, db_column='ReserveSpot', blank=True) # Field name made lowercase.
    enrolby = models.IntegerField(null=True, db_column='EnrolBy', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tKM_Enrolment_List'

class GsDelegates(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.DecimalField(decimal_places=0, null=True, max_digits=18, db_column='EEID', blank=True) # Field name made lowercase.
    superiorid = models.DecimalField(decimal_places=0, null=True, max_digits=18, db_column='SuperiorID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'GS_delegates'

class ThrLanguage(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    languagename = models.TextField(primary_key=True, db_column='LanguageName') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_Language'

class TkmTrainingmasterlist(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    trainingname = models.TextField(db_column='TrainingName') # Field name made lowercase.
    trtype = models.ForeignKey(TkmTrainingtype, null=True, db_column='TrType', blank=True) # Field name made lowercase.
    externaltr = models.BooleanField(null=True, db_column='ExternalTr', blank=True) # Field name made lowercase.
    deactivate = models.BooleanField(null=True, db_column='Deactivate', blank=True) # Field name made lowercase.
    tr_description = models.TextField(db_column='Tr_description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tKM_TrainingMasterList'

class ThrContracttype(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    contracttype = models.TextField(primary_key=True, db_column='ContractType') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_ContractType'

class Tbltools(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    tool_img = models.TextField(blank=True)
    tool_description = models.TextField(db_column='Tool_Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tbltools'

class ThrContractorprovider(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    provider = models.TextField(primary_key=True, db_column='Provider') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_ContractorProvider'

class TkmPrograms(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    programname = models.TextField(db_column='ProgramName') # Field name made lowercase.
    startdate = models.CharField(max_length=10, db_column='StartDate') # Field name made lowercase.
    enddate = models.CharField(max_length=10, db_column='EndDate', blank=True) # Field name made lowercase.
    loyalityagreement = models.BooleanField(null=True, db_column='LoyalityAgreement', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'tKM_Programs'

class TkmTrainerassigned(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    trainingid = models.IntegerField(null=True, db_column='TrainingID', blank=True) # Field name made lowercase.
    trainerid = models.IntegerField(null=True, db_column='TrainerID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tKM_TrainerAssigned'

class TblprojectTool(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    projectid = models.IntegerField(null=True, db_column='ProjectID', blank=True) # Field name made lowercase.
    project_id = models.TextField(blank=True)
    _toolid = models.TextField(db_column='_toolID', blank=True) # Field name made lowercase.
    toolid = models.IntegerField(null=True, db_column='toolID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblproject_tool'

class ThrFullparttime(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    timescale = models.TextField(primary_key=True, db_column='TimeScale') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_FullPartTime'

class TkmTrainingplans(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    programid = models.ForeignKey(TkmPrograms, db_column='ProgramID') # Field name made lowercase.
    trainingid = models.ForeignKey(TkmTrainingmasterlist, db_column='TrainingID') # Field name made lowercase.
    class Meta:
        db_table = u'tKM_TrainingPlans'

class Tblclients(models.Model):
    clientid = models.AutoField(db_column='clientID') # Field name made lowercase.
    clientname = models.CharField(max_length=250, db_column='clientName', blank=True) # Field name made lowercase.
    clientmru = models.CharField(max_length=250, db_column='clientMRU', blank=True) # Field name made lowercase.
    startdate = models.CharField(max_length=10, db_column='startDate', blank=True) # Field name made lowercase.
    description = models.TextField(blank=True)
    class Meta:
        db_table = u'tblClients'

class ThrEmployee(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName') # Field name made lowercase.
    lastname = models.TextField(db_column='LastName') # Field name made lowercase.
    fullname = models.TextField(db_column='FullName', blank=True) # Field name made lowercase.
    ntid = models.TextField(db_column='NTID', blank=True) # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_Employee'

class TblclientsBase(models.Model):
    clientid = models.AutoField(db_column='clientID') # Field name made lowercase.
    clientname = models.CharField(max_length=250, db_column='clientName', blank=True) # Field name made lowercase.
    clientlogo = models.CharField(max_length=250, db_column='clientLogo', blank=True) # Field name made lowercase.
    commiter = models.IntegerField(null=True, db_column='Commiter', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblClients_base'

class TkmTrainingvendors(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    vendorname = models.TextField(db_column='VendorName', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tKM_TrainingVendors'

class OpsEscalationsDetails(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    status = models.CharField(max_length=50, db_column='Status', blank=True) # Field name made lowercase.
    escalationrange = models.CharField(max_length=20, db_column='EscalationRange', blank=True) # Field name made lowercase.
    mru = models.CharField(max_length=80, db_column='MRU', blank=True) # Field name made lowercase.
    group = models.CharField(max_length=80, db_column='Group', blank=True) # Field name made lowercase.
    startdate = models.CharField(max_length=10, db_column='StartDate', blank=True) # Field name made lowercase.
    enddate = models.CharField(max_length=10, db_column='EndDate', blank=True) # Field name made lowercase.
    financialimpact = models.CharField(max_length=50, db_column='FinancialImpact', blank=True) # Field name made lowercase.
    owner = models.CharField(max_length=80, db_column='Owner', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=500, db_column='Description', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Ops_Escalations_Details'

class TkmProgramattendiees(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    programid = models.ForeignKey(TkmPrograms, db_column='ProgramID') # Field name made lowercase.
    eeid = models.ForeignKey(ThrEmployee, db_column='EEID') # Field name made lowercase.
    enrolmentdate = models.CharField(max_length=10, db_column='EnrolmentDate', blank=True) # Field name made lowercase.
    enrollereeid = models.IntegerField(null=True, db_column='EnrollerEEID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tKM_ProgramAttendiees'

class TkmExternaltrdetails(models.Model):
    id = models.ForeignKey(TkmTraininglist, primary_key=True, db_column='ID') # Field name made lowercase.
    vendorid = models.ForeignKey(TkmTrainingvendors, null=True, db_column='VendorID', blank=True) # Field name made lowercase.
    netamount = models.DecimalField(decimal_places=4, null=True, max_digits=10, db_column='NetAmount', blank=True) # Field name made lowercase.
    ownerid = models.ForeignKey(ThrEmployee, null=True, db_column='OwnerID', blank=True) # Field name made lowercase.
    errapproved = models.TextField(db_column='ERRApproved', blank=True) # Field name made lowercase.
    sbb = models.TextField(db_column='SBB') # Field name made lowercase.
    invoicedate = models.CharField(max_length=10, db_column='InvoiceDate', blank=True) # Field name made lowercase.
    invoicereceived = models.BooleanField(null=True, db_column='InvoiceReceived', blank=True) # Field name made lowercase.
    invoicenumber = models.TextField(db_column='InvoiceNumber', blank=True) # Field name made lowercase.
    comments = models.TextField(db_column='Comments', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tKM_ExternalTrDetails'

class Tbltowers(models.Model):
    tower_id = models.CharField(max_length=3, db_column='Tower_id', blank=True) # Field name made lowercase.
    tower_def = models.TextField(db_column='Tower_Def', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tbltowers'

class InnoProjectfiles(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    filename = models.TextField(db_column='Filename', blank=True) # Field name made lowercase. This field type is a guess.
    projectid = models.IntegerField(null=True, db_column='ProjectId', blank=True) # Field name made lowercase.
    commiter = models.ForeignKey(ThrEmployee, null=True, db_column='Commiter', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Inno_ProjectFiles'

class Tblsubprocesses(models.Model):
    subproc_id = models.CharField(max_length=40, blank=True)
    proc_id = models.CharField(max_length=40, blank=True)
    subproc_def = models.TextField(blank=True)
    class Meta:
        db_table = u'tblsubprocesses'

class Tblprojects(models.Model):
    ordering_col = models.IntegerField(null=True, db_column='Ordering_Col', blank=True) # Field name made lowercase.
    project_id = models.CharField(max_length=35, blank=True)
    client_name = models.CharField(max_length=45, db_column='Client_name', blank=True) # Field name made lowercase.
    project_name = models.CharField(max_length=35, db_column='Project_Name', blank=True) # Field name made lowercase.
    start_date = models.TextField(db_column='Start_Date', blank=True) # Field name made lowercase. This field type is a guess.
    end_date = models.TextField(db_column='End_Date', blank=True) # Field name made lowercase. This field type is a guess.
    ops_manager = models.CharField(max_length=35, db_column='Ops_Manager', blank=True) # Field name made lowercase.
    number_of_employees = models.IntegerField(null=True, db_column='Number_Of_Employees', blank=True) # Field name made lowercase.
    general_info = models.TextField(db_column='General_Info', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tblprojects'

class TblprojectProcesses(models.Model):
    id = models.IntegerField(null=True, blank=True)
    project_id = models.CharField(max_length=35, blank=True)
    tower = models.CharField(max_length=3, db_column='Tower', blank=True) # Field name made lowercase.
    process_id = models.CharField(max_length=40, blank=True)
    subproc_id = models.CharField(max_length=40, blank=True)
    class Meta:
        db_table = u'tblproject_processes'

class ThrTeamlist(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    teamname = models.TextField(primary_key=True, db_column='TeamName') # Field name made lowercase.
    parentmru = models.ForeignKey(ThrMru, null=True, db_column='ParentMRU', blank=True) # Field name made lowercase.
    supervisorid = models.IntegerField(null=True, db_column='SupervisorID', blank=True) # Field name made lowercase.
    tower = models.ForeignKey(ThrTower, null=True, db_column='Tower', blank=True) # Field name made lowercase.
    towerie = models.ForeignKey(TieTower, null=True, db_column='TowerIE', blank=True) # Field name made lowercase.
    teamleader = models.IntegerField(null=True, db_column='TeamLeader', blank=True) # Field name made lowercase.
    manager = models.ForeignKey(ThrEmployee, null=True, db_column='Manager', blank=True) # Field name made lowercase.
    opsmanager = models.ForeignKey(ThrEmployee, null=True, db_column='OpsManager', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_TeamList'

class TblprojectLanguage(models.Model):
    project_id = models.CharField(max_length=10, blank=True)
    lang_id = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = u'tblproject_language'

class TblprojectCountry(models.Model):
    project_id = models.CharField(max_length=10, blank=True)
    country_id = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = u'tblproject_country'

class Tblprocesses(models.Model):
    table_pk = models.IntegerField(null=True, blank=True)
    process_id = models.CharField(max_length=40, blank=True)
    tower_id = models.CharField(max_length=3, blank=True)
    process_def = models.TextField(blank=True)
    class Meta:
        db_table = u'tblprocesses'

class Tbllanguages(models.Model):
    lang_id = models.CharField(max_length=2, blank=True)
    language = models.CharField(max_length=10, db_column='Language', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tbllanguages'

class Tblcountries(models.Model):
    country_id = models.CharField(max_length=2, blank=True)
    country = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = u'tblcountries'

class TblSubprocAttributes(models.Model):
    subproc_id = models.CharField(max_length=40, blank=True)
    s_att_id = models.IntegerField(null=True, blank=True)
    s_att_name = models.CharField(max_length=45, blank=True)
    s_att_value = models.TextField(blank=True)
    proj_id = models.CharField(max_length=35, blank=True)
    s_att_description = models.TextField(blank=True)
    class Meta:
        db_table = u'tbl_subproc_attributes'

class TkmBlacklist(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.ForeignKey(ThrEmployee, null=True, db_column='EEID', blank=True) # Field name made lowercase.
    startdate = models.CharField(max_length=10, db_column='StartDate', blank=True) # Field name made lowercase.
    enddate = models.CharField(max_length=10, db_column='EndDate', blank=True) # Field name made lowercase.
    blacklistedby = models.CharField(max_length=10, db_column='BlacklistedBy', blank=True) # Field name made lowercase.
    blacklister = models.IntegerField(null=True, db_column='BlackLister', blank=True) # Field name made lowercase.
    balcklisted_fortraining = models.ForeignKey(TkmTraininglist, null=True, db_column='Balcklisted_forTraining', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tKM_BlackList'

class VolValues(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    value = models.FloatField(db_column='Value') # Field name made lowercase.
    data_type = models.ForeignKey(VolDatatypes, db_column='Data_Type') # Field name made lowercase.
    mru = models.TextField(db_column='MRU') # Field name made lowercase.
    comiter_eeid = models.ForeignKey(ThrEmployee, db_column='Comiter_EEID') # Field name made lowercase.
    value_formonth = models.CharField(max_length=10, db_column='Value_ForMonth', blank=True) # Field name made lowercase.
    comitteddate = models.TextField(db_column='ComittedDate') # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'Vol_Values'

class InnoSpocs(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.IntegerField(null=True, db_column='EEID', blank=True) # Field name made lowercase.
    active = models.BooleanField(null=True, db_column='Active', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Inno_SPOCs'

class ThrEelanguages(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.ForeignKey(ThrEmployee, null=True, db_column='EEID', blank=True) # Field name made lowercase.
    langspoken = models.ForeignKey(ThrLanguage, null=True, db_column='LangSpoken', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_EELanguages'

class VolProcTowers(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    tower_name = models.TextField(db_column='Tower_Name') # Field name made lowercase.
    process_n = models.TextField(db_column='Process_n') # Field name made lowercase.
    class Meta:
        db_table = u'Vol_Proc_Towers'

class VolPolicy(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    datatype = models.ForeignKey(VolDatatypes, db_column='DataType_ID') # Field name made lowercase.
    commiter_eeid = models.ForeignKey(ThrEmployee, db_column='Commiter_EEID') # Field name made lowercase.
    mru = models.TextField(db_column='MRU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Vol_Policy'

class ThrOpsmru(models.Model):
    id = models.ForeignKey(ThrEmployee, primary_key=True, db_column='ID') # Field name made lowercase.
    mru = models.ForeignKey(ThrMru, null=True, db_column='MRU', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_OpsMRU'

class Tblusers(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50, db_column='First Name', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    last_name = models.CharField(max_length=50, db_column='Last Name', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    password = models.CharField(max_length=100, db_column='Password', blank=True) # Field name made lowercase.
    is_active = models.SmallIntegerField(null=True, db_column='Is_Active', blank=True) # Field name made lowercase.
    user_type = models.CharField(max_length=11, db_column='User_Type', blank=True) # Field name made lowercase.
    user_eeid = models.IntegerField(db_column='User_EEID') # Field name made lowercase.
    class Meta:
        db_table = u'tblusers'

class VolMarkets(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    market_name = models.TextField(db_column='Market_Name') # Field name made lowercase.
    class Meta:
        db_table = u'Vol_Markets'

class TkmTrainingtype(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    tfamily = models.TextField(db_column='TFamily', blank=True) # Field name made lowercase.
    ttype = models.TextField(primary_key=True, db_column='TType') # Field name made lowercase.
    class Meta:
        db_table = u'tKM_TrainingType'

class VolDatatypes(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    datatypecategory = models.ForeignKey(VolDatatypeCateg, db_column='DataTypeCategory_ID') # Field name made lowercase.
    processtower = models.ForeignKey(VolProcTowers, db_column='ProcessTower_ID') # Field name made lowercase.
    market = models.ForeignKey(VolMarkets, db_column='Market_ID') # Field name made lowercase.
    value_type = models.TextField(db_column='Value_type') # Field name made lowercase.
    createdby = models.IntegerField(null=True, db_column='CreatedBy', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Vol_DataTypes'

class VolDatatypeCateg(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    categname = models.TextField(db_column='CategName') # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase. This field type is a guess.
    addedby = models.IntegerField(null=True, db_column='AddedBy', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Vol_DataType_Categ'

class ThrAdditionalinfo(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.ForeignKey(ThrEmployee, null=True, db_column='EEID', blank=True) # Field name made lowercase.
    internalfunction = models.ForeignKey(ThrInternalfunction, null=True, db_column='InternalFunction', blank=True) # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True) # Field name made lowercase.
    startdate = models.CharField(max_length=10, db_column='StartDate') # Field name made lowercase.
    enddate = models.CharField(max_length=10, db_column='EndDate') # Field name made lowercase.
    modifieddate = models.CharField(max_length=10, db_column='ModifiedDate', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'tHR_AdditionalInfo'

class TkmTrainingrequests(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.ForeignKey(ThrEmployee, db_column='EEID') # Field name made lowercase.
    trcat = models.ForeignKey(TkmTrainingmasterlist, db_column='TrCat_ID') # Field name made lowercase.
    registerdate = models.CharField(max_length=10, db_column='RegisterDate') # Field name made lowercase.
    class Meta:
        db_table = u'tKM_TrainingRequests'

class VolCommiters(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    eeid = models.IntegerField(db_column='EEID') # Field name made lowercase.
    mru = models.TextField(db_column='MRU') # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive') # Field name made lowercase.
    class Meta:
        db_table = u'Vol_Commiters'

class TallDelegates(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    mainaccount = models.ForeignKey(ThrEmployee, null=True, db_column='MainAccount', blank=True) # Field name made lowercase.
    assigneddelegate = models.ForeignKey(ThrEmployee, null=True, db_column='AssignedDelegate', blank=True) # Field name made lowercase.
    startdelegate = models.TextField(db_column='StartDelegate') # Field name made lowercase. This field type is a guess.
    enddelegate = models.TextField(db_column='EndDelegate', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'tAll_Delegates'

class ThrDatetypes(models.Model):
    id = models.AutoField(db_column='ID') # Field name made lowercase.
    datetype = models.TextField(primary_key=True, db_column='DateType') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_DateTypes'

class ThrDatespecs(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    empid = models.ForeignKey(ThrEmployee, null=True, db_column='EmpID', blank=True) # Field name made lowercase.
    datetype = models.ForeignKey(ThrDatetypes, null=True, db_column='DateType', blank=True) # Field name made lowercase.
    datevalue = models.CharField(max_length=10, db_column='DateValue') # Field name made lowercase.
    class Meta:
        db_table = u'tHR_DateSpecs'

class VolProcesses(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID') # Field name made lowercase.
    process_name = models.TextField(db_column='Process_Name') # Field name made lowercase.
    class Meta:
        db_table = u'Vol_Processes'

