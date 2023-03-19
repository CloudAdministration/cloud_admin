"""
    This module defines two views for the cloud_admin application:

    index: renders the index.html template with a welcome message
    hello_user: renders the hello_user.html template with a welcome message
"""
from django.shortcuts import render


def index(request):
    """
    Renders the index.html template with a welcome message.
    Args:
        request (HttpRequest): HTTP request object.

    Returns:
        HttpResponse: HTTP response object with the rendered HTML template.
    """

    return render(request, 'cloud_admin/index.html', {
        'welcome_message': 'Hello!'
    })


def hello_user(request):
    """
    Renders the hello_user.html template with a welcome message.
    Args:
        request (HttpRequest): HTTP request object.

    Returns:
        HttpResponse: HTTP response object with the rendered HTML template.
    """
    return render(request, 'cloud_admin/hello_user.html', {
        'welcome_message': 'Hello'
    })
