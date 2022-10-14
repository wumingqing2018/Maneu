from common.models import ManeuClass


def class_list(user_id=''):
    return ManeuClass.objects.filter(user_id=user_id).all()
