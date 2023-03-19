#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cloud_admin.settings')

    #Check DJANGO_SETTINGS_MODULE configuration
    #if os.environ.get('DJANGO_SETTINGS_MODULE'):
        # If `subcommand` is missing due to misconfigured settings, the
        # following line will retrigger an ImproperlyConfigured exception
        # (get_commands() swallows the original one) so the user is
        # informed about it.
        #sys.stderr.write("SETTINGS: "+os.environ.get('DJANGO_SETTINGS_MODULE')+'\n')
    #else:
        #sys.stderr.write("No Django settings specified.\n")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
