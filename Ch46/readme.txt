Chapter 46 - HttpResponse.set_cookie()
=======================================

What is a cookie?
-----------------
A cookie is a small piece of text (key=value) that the SERVER asks the
BROWSER to save. After that, the browser automatically sends it back with
every request to the same site. So the server can "remember" something
about the visitor (theme, last visited page, language, etc.).

Flow:
  1. Browser -> GET /set/             (no cookie yet)
  2. Server  -> response + header:    Set-Cookie: student_name=Ali
  3. Browser saves it
  4. Browser -> GET /get/  + header:  Cookie: student_name=Ali
  5. Server reads it from request.COOKIES


response.set_cookie(
    key,              # cookie name
    value='',         # always stored as a string
    max_age=None,     # lifetime in seconds, e.g. 60*60*24 = 1 day
    expires=None,     # or an exact datetime instead of max_age
    path='/',         # which URLs receive the cookie
    domain=None,      # which domain (None = current site only)
    secure=False,     # True = only sent over HTTPS
    httponly=False,   # True = JavaScript (document.cookie) cannot read it
    samesite=None,    # 'Lax', 'Strict' or 'None' (cross-site rules)
)

