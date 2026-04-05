import sys

if sys.version_info >= (3, 12):
    from .init_once_3_12 import init_once

else:
    from.init_once_3_8 import init_once


__all__ = ["init_once"]