def assign_user_fields(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return

    fields = {
        'email': details.get('email'),
        'full_name': details.get('fullname') or details.get('first_name'),
        'phone': None  # Do NOT assign email to phone!
    }
    return {'user': strategy.create_user(**fields)}
