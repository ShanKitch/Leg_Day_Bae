from django import template

register = template.Library()

def decode_workout_types(types):
    """
    Decode workout types
    """
    workouts = (
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
    decoder = dict(workouts)
    decoded = [decoder[t] for t in types.split(",")]
    decoded.sort()
    return ','.join(decoded)

register.filter('decode_workout_types', decode_workout_types)