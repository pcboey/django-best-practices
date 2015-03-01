from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# host/domain names that this Django site can serve.
# This is a security measure to prevent an attacker 
# from poisoning caches and password reset emails 
# with links to malicious hosts 
# by submitting requests with a fake HTTP Host header
# www.mysite.com will be matched against the request’s Host header exactly 
# .mysite.com will match mysite.com, www.mysite.com and any subdomain
ALLOWED_HOSTS = [".mysite.com"]

STATIC_ROOT = os.path.join(BASE_DIR, 'sitestatic')
