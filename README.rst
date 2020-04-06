=================
kp_static_version
=================

kp_static_version is a simple Django app to add
a version number to static files and force browsers to use the latest version of the file.


Quick start
-----------

1. Install django-kp-static-version::

    pip install django-kp-static-version

2. Add "kp_static_version" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'kp_static_version',
    ]

3. Load templatetags into your template::

    {% load kp_static %}


4. Load your static file::

    <script src="{% vstatic "js/sample.js" %}"></script>

If in your settings.py the variable **DEBUG = True** then a *random number* will be generated
for development otherwise the value **KP_STATIC_VERSION** will be used::

    KP_STATIC_VERSION = "0.5"

The result::

    <script src="/static/js/sample.js?v=0.5"></script>

