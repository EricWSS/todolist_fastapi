from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address, default_limits=["20/minute"]) # 1 request por minuto de acordo com o usuário.
