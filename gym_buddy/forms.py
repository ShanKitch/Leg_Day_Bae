from django import forms
from django.forms import ModelForm
from .models import Profile, Forum_Message




exercise_choices = (
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

frequency_choices=(
    ('1', '1-2 Times Per Week'),
    ('2', '2-3 Times Per Week'),
    ('3', '3-4 Times Per Week'),
    ('4', '4-5 Times Per Week'),
    ('5', '5+ Times Per Week')
)

time_choices=(
    ('1', 'Morning'),
    ('2', 'Afternoon'),
    ('3', 'Evening'),
    ('4', 'Flexible')
)

sex_choices=(
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










class ProfileForm(forms.Form):
    workout_type = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=exercise_choices,
        
       
        
    )


    new_exercise=forms.CharField(max_length=50, required=False)
    frequency=forms.MultipleChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=frequency_choices,
    )

    time_day=forms.MultipleChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=time_choices,
    )
    age=forms.IntegerField(required=True)
    sex=forms.MultipleChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=sex_choices,
    )
    location_city=forms.CharField(max_length=50, required=True)
    location_state=forms.ChoiceField(
        required=True,
        choices=states
    )
    img=forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = '__all__'

class PartialProfileForm(forms.ModelForm):
    new_exercise=forms.CharField(max_length=50, required=False)
    frequency=forms.MultipleChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=frequency_choices,
    )

    time_day=forms.MultipleChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=time_choices,
    )
    age=forms.IntegerField(required=True)
    sex=forms.MultipleChoiceField(
        required=True,
        widget=forms.RadioSelect,
        choices=sex_choices,
    )
    location_city=forms.CharField(max_length=50, required=True)
    location_state=forms.ChoiceField(
        required=True,
        choices=states
    )
    img=forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['owner', 'new_exercise', 'frequency', 'time_day', 'age', 'sex', 'location_city', 'location_state', 'img']

class ForumMessageForm(forms.Form):
    message_subject=forms.CharField(max_length=50, required=True)
    forum_message=forms.CharField(max_length=250, required=True) 

    class Meta:
        model = Forum_Message
        fields = '__all__'