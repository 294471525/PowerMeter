#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import requests
from time import sleep


def enable_undeadthread():
    cnt = 10
    while cnt:
        try:
            requests.get("http://192.168.0.101:8000/startService", )
        except Exception:
            cnt -= 1
            sleep(1)
        else:
            break


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PyServer.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    import threading
    threading.Thread(target=enable_undeadthread, daemon=True).start()
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
