def user_listing_path(instance, filename):
    return f'user_{instance.user.id}/listings/{filename}'