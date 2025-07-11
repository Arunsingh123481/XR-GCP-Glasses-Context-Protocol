from flask import request, abort
import functools

# Dummy user consent (in real app, ask and store)
user_has_consented = True

def require_consent(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not user_has_consented:
            abort(403, description="User consent required.")
        return func(*args, **kwargs)
    return wrapper
