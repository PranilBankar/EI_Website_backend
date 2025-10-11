import os
import sys
import django

# Add the parent directory (the one that contains manage.py) to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Tell Django where the settings module is
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'engineeringindia.settings')

# Initialize Django
django.setup()
from django.contrib.auth.models import User
from api.models import Event

def run():
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "adminpass")
        print("Created admin/adminpass")
    now = timezone.now()
    Event.objects.get_or_create(
        slug="welcome-meet",
        defaults={
            "title":"Welcome Meet",
            "description":"Welcome to Engineering India RBU.",
            "start_time": now + timedelta(days=7),
            "location":"Main Auditorium",
            "capacity":100
        }
    )
    print("Seed done")

if __name__ == "__main__":
    run()

