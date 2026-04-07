from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="tyche_User",
        email="anjalishyju12gmail.com",
        password="tychepassword"
    )
    print("Superuser created")
else:
    print("Superuser already exists")