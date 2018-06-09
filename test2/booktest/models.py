from django.db import models
import sys

reload(sys)

sys.setdefaultencoding('utf-8')
# Create your models here.
class BookInfoManager(models.Manager):
    def get_queryset(self):
        """It means that the future query set based on this query set"""
        return super(BookInfoManager,self).get_queryset().filter(isDelete = False)

    def create(self, title, pub_date):
        book = BookInfo()
        book.btitle = title
        book.bpub_date = pub_date
        book.bread = 0
        book.bcomment = 0
        book.isDelete = False
        return book


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'bookinfo'
    #your manager
    books1 = models.Manager() #default manager was overwrited  BookInfo.objects.all() was overwrited

    books2 = BookInfoManager() #use:BookInfo.books2.all()

    @classmethod
    def create(cls, title, pub_date):
        book = BookInfo()
        book.btitle = title
        book.bpub_date = pub_date
        book.bread = 0
        book.bcomment = 0
        book.isDelete = False
        return book
    def __str__(self):
        return self.btitle.encode('utf-8')





class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField(default=True)
    hcontent = models.CharField(max_length=1000)
    isDelete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo)

    def __str__(self):
        return self.hname.encode('utf-8')

class AreaInfo(models.Model):
    atitle = models.CharField(max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True)

    #up level:area.aParent
    #down level: area.areainfo_set.all()
    def __str__(self):
        return self.atitle.encode('utf-8')




