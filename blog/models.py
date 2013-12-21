from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User)
    

    # creator = models.ForeignKey(User) 
    create_time = models.DateField()
    # sove_time = models.DateField(null=True,blank=True)
    # point = models.IntegerField()
    # solver = models.ForeignKey(User)
    # sove_status = models.IntegerField(default=0)



#     def __unicode__(self):
#         return str(self.id)+str(self.user.id)+str(self.point)
    
#     def sove(self):
#         now = datetime.datetime.now()
#     	self.sove_tlime = now
#     	sove_status = 1 #~  1 is done
#     	self.save()
#     def add_point(self):

#     def confirm_share(self):
#         self.share_status = 2
#         self.save()
        
#     def get_borrow_period(self):        
#         return (self.return_time - self.borrow_time).days    
        
#     def get_keep_period(self):               
#         return 30-(datetime.datetime.now().date() - self.borrow_time).days
        
#     class Meta:
#         db_table = "task"
#         ordering = ['-create_time']













