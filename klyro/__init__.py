try:
    from klyro._version import __version__
except ImportError:
    try:
        from importlib.metadata import version

        __version__ = version("klyro")
    except ImportError:
        __version__ = "0+unknown"

__all__ = ["__version__"]
