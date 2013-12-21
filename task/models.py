from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.shortcuts import get_object_or_404
# Create your models here.
class Task(models.Model):
    creator = models.ForeignKey(User) 
    create_time = models.DateField()
    task_title = models.CharField(max_length=255)
    task_content = models.CharField(max_length=255,blank=True)
    solve_time = models.DateField(null=True,blank=True)
    point = models.IntegerField()
    #solver = models.ForeignKey(User)
    solver_id = models.IntegerField()
    solve_status = models.IntegerField(default=0)



    def __unicode__(self):
        return str(self.id)+str(self.creator.id)+str(self.point)
    
    # def sove(self):
    #     now = datetime.datetime.now()
    #     self.solve_tlime = now
    #     solve_status = 1 #~  1 is done
    #     self.save()
    #def add_point(self):

    # def confirm_share(self):
    #     self.share_status = 2
    #     self.save()
        
    # def get_borrow_period(self):        
    #     return (self.return_time - self.borrow_time).days    
        
    # def get_keep_period(self):               
    #     return 30-(datetime.datetime.now().date() - self.borrow_time).days
        
    class Meta:
        db_table = "task"
        ordering = ['-create_time']
class Task_admin(admin.ModelAdmin):
    list_display=('id','creator','create_time','solve_time','point','solver_id','solve_status')

def get_unsolved_task():
    return Task.objects.filter(solve_status=0)
def get_soved_task():
    return Task.objects.filter(solve_status=1)
def get_task_by_id(id):
    return get_object_or_404(Task, id=id)











class UserPoint(models.Model):
    user = models.ForeignKey(User)
    point = models.IntegerField(default=0)
    task = models.ForeignKey(Task)
    solve_time = models.DateField(null=True,blank=True)


    def __unicode__(self):
        return str(self.id)+str(self.user.id)+str(self.point)+str(self.task.id)
    class Meta:
        db_table = "userpoint"

    # def add_point(self, point):
    #     self.point += point
    #     self.save()
class UserPoint_admin(admin.ModelAdmin):
    list_display=('id','point')#,'task','solve_time')
# def sort_user_point():
#     return UserPoint.all().order("point")

# def get_new_task():
#     return Task.objects.filter(solve_status=0)    

# def get_soved_task():   
#     return Task.objects.filter(solve_status=1)

# def get_month_winner():
#     current_month = get_current_month()
#     return UserPont.objects.filter(solve_time__month=current_month).order("point")






















