from django.utils.translation import gettext_lazy as _


def assign_user_fields(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return

    fields = {
        'email': details.get('email'),
        'full_name': details.get('fullname') or details.get('first_name'),
        'phone': None
    }
    return {'user': strategy.create_user(**fields)}
