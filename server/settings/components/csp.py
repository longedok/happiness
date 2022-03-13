"""
This file contains a definition for Content-Security-Policy headers.

Read more about it:
https://developer.mozilla.org/ru/docs/Web/HTTP/Headers/Content-Security-Policy

We are using `django-csp` to provide these headers.
Docs: https://github.com/mozilla/django-csp
"""

CSP_SCRIPT_SRC = ("'self'", "'unsafe-eval'", "'unsafe-inline'", "cdn.jsdelivr.net", "unpkg.com")
CSP_SCRIPT_SRC_ELEM = ("'self'", "'unsafe-inline'", "cdn.jsdelivr.net", "unpkg.com")
CSP_IMG_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'", "cdn.jsdelivr.net")
CSP_STYLE_SRC = ("'self'", "cdn.jsdelivr.net")
CSP_DEFAULT_SRC = ("'none'",)
CSP_CONNECT_SRC = ("'self'",)
CSP_MEDIA_SRC = ("audio.oxforddictionaries.com",)
