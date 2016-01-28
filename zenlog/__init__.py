#!/usr/bin/env python
import logging
import colorlog

# a theme is just a dict of strings to represent each level
THEME = {logging.CRITICAL: " [!!!!!] ",
         logging.ERROR:    "  [!!!]  ",
         logging.WARNING:  "   [!]   ",
         logging.INFO:     "    i    ",
         logging.DEBUG:    "   ...   "}

# this class holds all the logic; see the end of the script to
# see how it's instantiated in order to have the line
# "from zenlog import log" work
class Log:
    def __init__(self, lvl=logging.DEBUG, format=None):
        self._lvl = lvl
        if not format:
            self.format = "  %(log_color)s%(styledname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"
        logging.root.setLevel(self._lvl)
        self.formatter = colorlog.ColoredFormatter(self.format)
        self.stream = logging.StreamHandler()
        self.stream.setLevel(self._lvl)
        self.stream.setFormatter(self.formatter)
        self.logger = logging.getLogger('pythonConfig')
        self.logger.setLevel(self._lvl)
        self.logger.addHandler(self.stream)
        self.theme = THEME
        self.extra = {"styledname": self.theme[self._lvl]}

    # the magic happens here: we use the "extra" argument documented in
    # https://docs.python.org/2/library/logging.html#logging.Logger.debug
    # to inject new items into the logging.LogRecord objects
    # we also create our convenience methods here
    def critical(self, message, *args, **kwargs):
        for line in str(message).splitlines():
            self.logger.critical(line,
                                 extra={"styledname": self.theme[logging.CRITICAL]},
                                 *args, **kwargs)
    crit = c = fatal = critical
    def error(self, message, *args, **kwargs):
        for line in str(message).splitlines():
            self.logger.error(line,
                              extra={"styledname": self.theme[logging.ERROR]},
                              *args, **kwargs)
    err = e = error
    def warn(self, message, *args, **kwargs):
        for line in str(message).splitlines():
            self.logger.warn(line,
                             extra={"styledname": self.theme[logging.WARNING]},
                             *args, **kwargs)
    warning = w = warn
    def info(self, message, *args, **kwargs):
        for line in str(message).splitlines():
            self.logger.info(line,
                             extra={"styledname": self.theme[logging.INFO]},
                             *args, **kwargs)
    inf = nfo = i = info
    def debug(self, message, *args, **kwargs):
        for line in str(message).splitlines():
            self.logger.debug(line,
                              extra={"styledname": self.theme[logging.DEBUG]},
                              *args, **kwargs)
    dbg = d = debug

    # other convenience functions to set the global logging level
    def _parse_level(self, lvl):
        if lvl == logging.CRITICAL or lvl in ("critical", "crit", "c", "fatal"):
            return logging.CRITICAL
        elif lvl == logging.ERROR or lvl in ("error", "err", "e"):
            return logging.ERROR
        elif lvl == logging.WARNING or lvl in ("warning", "warn", "w"):
            return logging.WARNING
        elif lvl == logging.INFO or lvl in ("info", "inf", "nfo", "i"):
            return logging.INFO
        elif lvl == logging.DEBUG or lvl in ("debug", "dbg", "d"):
            return logging.DEBUG
        else:
            raise TypeError("Unrecognized logging level: %s" % lvl)

    def level(self, lvl=None):
        '''Get or set the logging level.'''
        if not lvl:
            return self._lvl
        self._lvl = self._parse_level(lvl)
        self.stream.setLevel(self._lvl)
        logging.root.setLevel(self._lvl)

log = Log()
