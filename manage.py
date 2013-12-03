#!/usr/bin/env python
import os
import sys

if os.environ.get('THINKCRUNCH_LOCAL'):
    environment = "thinkcrunch.settings.dev"
elif os.environ.get('THINKCRUNCH_STAGING'):
    environment = "thinkcrunch.settings.staging"
elif os.environ.get('THINKCRUNCH_PRODUCTION'):
    environment = "thinkcrunch.settings.production"
                       
if __name__ == "__main__":
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 
                       environment)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
