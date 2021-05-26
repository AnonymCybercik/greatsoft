from django.db import models


######### BLOG MODEL ############
class Blog(models.Model):
    blog_title = models.CharField(max_length = 30,null = True,blank = True)
    blog_describtion = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.blog_title

##################################


########## CONTACT MODEL #########

class Contact(models.Model):
    name = models.CharField(max_length = 50,null = True,blank = True)
    phone = models.IntegerField(null = True,blank = True)
    message = models.TextField(null = True,blank = True)

    def __str__(self):
        return self.name


########## PORTFOLIO MODEL #############


class Portfolio(models.Model):

    choice = [
        ("Website","Website"),
        ("mobile","mobile"),
        ("Design","Design"),
        ("TGBot","TGBot"),
    ]
    complany_name = models.TextField(null = True,blank = True)
    web_site = models.CharField(max_length = 30, null = True,blank = True)
    portfolio_image = models.FileField(upload_to = 'portfolio-images/',null = True,blank = True)
    category = models.CharField(max_length=50,choices = choice, null = True,blank = True)
    
    def __str__(self):
        return self.complany_name


##################################################