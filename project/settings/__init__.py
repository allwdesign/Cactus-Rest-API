import os

if os.getenv('DJANGO_LOCAL') is not None:
	from .local import *

if os.getenv('DJANGO_DEVELOPMENT') is not None:
	from .dev import *

if os.getenv('DJANGO_PRODUCTION') is not None:
	from .prod import *