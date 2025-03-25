"""
Run script for Gamers Insight Django application with Python 3.13 compatibility
"""
import sys
import os

# Apply the compatibility patch
import django_compat

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'game_insight.settings')

# Run the Django management command
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    try:
        execute_from_command_line(sys.argv)
    except Exception as e:
        print(f"Error running Django: {e}")