import os
import django

# ✅ SET YOUR PROJECT NAME HERE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tyche_web.settings')

# ✅ INITIALIZE DJANGO
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser(
        username="admin",
        email="admin@gmail.com",
        password="admin123"
    )
    print("✅ Superuser created")
else:
    print("⚠️ Superuser already exists")