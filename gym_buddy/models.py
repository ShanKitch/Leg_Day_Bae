from django.db import models
from django.forms import ModelForm
import bcrypt
import re



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors={}
        if len(postData['first_name'])==0:
            errors['first_name']= 'First name is required!' 
        elif len(postData['first_name']) <2 or postData['first_name'].isalpha() != True:
            errors['first_name']= 'First name must be at least 2 characters long, and contain only letters'
        if len(postData['last_name'])==0:
            errors['last_name']= 'Last name is required!' 
        elif len(postData['last_name']) <2 or postData['last_name'].isalpha() != True:
            errors['last_name']= 'Last name must be at least 2 characters long, and contain only letters'
        if len(postData['email'])==0:
            errors['email']='Email is required'
        elif not EMAIL_REGEX.match(postData['email']):               
            errors['email'] = "Invalid email address!"
        existing_user=User.objects.filter(email=postData['email'])
        if len(existing_user) > 0:
            errors['email'] = "Email already in use"
        existing_username=User.objects.filter(username=postData['username'])
        if len(existing_username) > 0:
            errors['username'] ="Username already in use"
        if len(postData['password'])==0:
            errors['password']= 'Password is required'
        elif len(postData['password'])<8:
            errors['password'] = 'Password must be at least 8 characters long'
        elif postData['password'] != postData['confirm_password']:
            errors ['password']= "Password and Confirm Password inputs must match"
        return errors

    def log_validator(self, postData):
        errors={}
        if len(postData['email'])==0:
            errors['email']='Email is required'
        elif not EMAIL_REGEX.match(postData['email']):               
            errors['email'] = "Invalid email address!"
        if len(postData['password'])==0:
                errors['password']= 'Password is required'
        elif len(postData['password'])<8:
            errors['password'] = 'Password must be at least 8 characters long'
        existing_user=User.objects.filter(email=postData['email'])
        if len(existing_user) != 1:
            errors['email']="User Not Found"
        elif bcrypt.checkpw(postData['password'].encode(), existing_user[0].password.encode()) != True:
            errors['email']="Email and Passwords do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()

exercise = (
    ('1','Running'),
    ('2','Weight Training'),
    ('3', 'HIIT'),
    ('4', 'Yoga'),
    ('5', 'Pilates'),
    ('6', 'Crossfit'),
    ('7','Dance Fitness'),
    ('8', 'Cycling'),
    ('9', 'Aerobics'),
    ('10', 'Swimming')
)


frequency=(
    ('1', '1-2 Times Per Week'),
    ('2', '2-3 Times Per Week'),
    ('3', '3-4 Times Per Week'),
    ('4', '4-5 Times Per Week'),
    ('5', '5+ Times Per Week')
)

time=(
    ('1', 'Morning'),
    ('2', 'Afternoon'),
    ('3', 'Evening'),
    ('4', 'Flexible')
)

sex=(
    ('1', 'Male'),
    ('2', 'Female'),
    ('3', 'Prefer Not to Say')
)

states=(
    ('1', 'AL'),
    ('2', 'AK'),
    ('3', 'AZ'),
    ('4','AK'),
    ('5', 'CA'),
    ('6', 'CO'),
    ('7', 'CT'),
    ('8', 'DC'),
    ('9', 'DE'),
    ('10', 'FL'),
    ('11', 'GA'),
    ('12', 'HI'),
    ('13', 'ID'),
    ('14', 'IL'),
    ('15', 'IN'),
    ('16', 'IA'),
    ('17', 'KS'),
    ('18', 'KY'),
    ('19', 'LA'),
    ('20', 'ME'),
    ('21', 'MD'),
    ('22', 'MA'),
    ('23' , 'MI'),
    ('24', 'MN'),
    ('25', 'MS'),
    ('26', 'MO'),
    ('27','MT'),
    ('28', 'NE'),
    ('29', 'NV'),
    ('30', 'NH'),
    ('31', 'NJ'),
    ('32', 'NM'),
    ('33', 'NY'),
    ('34', 'NC'),
    ('35', 'ND'),
    ('36', 'OH'),
    ('37', 'OK'),
    ('38', 'OR'),
    ('39', 'PA'),
    ('40', 'RI'),
    ('41', 'SC'),
    ('42', 'SD'),
    ('43', 'TN'),
    ('44', 'TX'),
    ('45', 'UT'),
    ('46', 'VT'),
    ('47', 'VA'),
    ('48', 'WA'),
    ('49', 'WV'),
    ('50', 'WI'),
    ('51', 'WY')

)

class ProfileManager(models.Manager):
    def profile_validator(self, postData):
        errors={}
        if len(postData['frequency'])==0:
            errors['frequency']='Workout Frequency Is A Required Field'
        if len(postData['time_day'])==0:
                errors['time_day']= 'Preferred Workout Time Is A Required Field'
        if len(postData['age'])==0:
                errors['age']= 'Age Is A Required Field'
        if len(postData['sex'])==0:
                errors['sex']= 'Sex Is A Required Field'
        if len(postData['location_city'])==0:
                errors['location_city']="City Is A Required Field"
        if len(postData['location_state'])==0:
                errors['location_state']= 'State Is A Required Field'
        return errors



class Profile(models.Model):
    owner=models.ForeignKey(User, related_name="my_profile", on_delete=models.CASCADE)
    workout_type=models.CharField(max_length=255, choices=exercise)
    new_exercise=models.CharField(max_length=50)
    frequency=models.CharField(max_length=50, choices=frequency)
    time_day=models.CharField(max_length=50, choices=time)
    age=models.IntegerField()
    sex=models.CharField(max_length=50, choices=sex)
    location_city=models.CharField(max_length=50)
    location_state=models.CharField(max_length=2, choices=states) 
    img=models.ImageField(upload_to="images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ProfileManager()

    # def __str__(self):
    #         return self.name + ": " + str(self.imagefile)
    


class Exercise(models.Model):
    name=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profiles=models.ManyToManyField(Profile, related_name="fav_exercises")
    
class Message(models.Model) : 
    message=models.TextField()
    subject=models.CharField(max_length=50)
    sender=models.ForeignKey(User, related_name='sent_from', on_delete=models.CASCADE)
    recipient=models.ForeignKey(User, related_name='sent_to', on_delete=models.CASCADE)
    read=models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Forum_Message(models.Model):
    message_subject=models.CharField(max_length=75)
    forum_message=models.CharField(max_length=255)
    poster=models.ForeignKey(User, related_name='user_posts', on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name='liked_posts')
    time_stamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Forum_Comment(models.Model):
    comment=models.CharField(max_length=255)
    poster=models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    forum_message=models.ForeignKey(Forum_Message, related_name="post_comments", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment_Reply(models.Model):
    reply_comment=models.CharField(max_length=255)
    poster=models.ForeignKey(User, related_name='user_replies', on_delete=models.CASCADE) 
    forum_comment=models.ForeignKey(Forum_Comment, related_name="reply_comments", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  








# Create your models here.
