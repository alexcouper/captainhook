from pkg_resources import get_distribution, DistributionNotFound

__project__ = 'captainhook'
__version__ = None

try:
    __version__ = get_distribution(__project__).version
except DistributionNotFound:
    VERSION = __project__ + '-' + '(local)'
else:
    VERSION = __project__ + '-' + __version__
