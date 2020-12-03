
from .models import Profile
import django_filters

class ProfileFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = ['owner', 'workout_type', 'new_exercise', 'frequency', 'time_day', 'age', 'sex', 'location_city', 'location_state' ]