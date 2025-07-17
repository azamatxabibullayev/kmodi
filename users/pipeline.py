from users.models import User


def assign_user_fields(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {'user': user}

    email = details.get('email')
    full_name = details.get('fullname') or details.get('first_name')

    if not email:
        return
    try:
        existing_user = User.objects.get(email=email)
        return {'user': existing_user}
    except User.DoesNotExist:
        new_user = strategy.create_user(
            email=email,
            full_name=full_name or email,
            phone=None,
            role='student'
        )
        return {'user': new_user}
