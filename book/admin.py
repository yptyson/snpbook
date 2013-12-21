from django.contrib import admin
from snpbook.book.models import Book,Book_admin,Borrow,Borrow_admin#,BookStatus,BookStatus_admin
#from snpbook.book.models import ReadHistory,ReadHistory_admin
from snpbook.room.models import Room,Room_admin
from snpbook.members.models import Member, Member_admin
from snpbook.task.models import  UserPoint, UserPoint_admin
from snpbook.task.models import Task, Task_admin
admin.site.register(Book, Book_admin)
admin.site.register(Borrow, Borrow_admin)
admin.site.register(Room, Room_admin)
admin.site.register(Member, Member_admin)
admin.site.register(UserPoint, UserPoint_admin)
admin.site.register(Task, Task_admin)