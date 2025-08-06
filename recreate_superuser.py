import os
import django
from django.contrib.auth import get_user_model

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_notesapp.settings")
django.setup()

User = get_user_model()
username = "legacyblue"
password = "root"
email = "farananijoshua@gmail.com"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, password=password, email=email)
    print("✅ Superuser created successfully.")
else:
    print("⚠️ Superuser already exists.")
