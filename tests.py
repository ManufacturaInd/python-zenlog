import zenlog
import logging
import unittest


class TestSetLevelMethods(unittest.TestCase):
    def setUp(self):
        self.log = zenlog.log

    def set_level(self, level, logging_level):
        self.log.level(level)
        return self.log.level() == logging_level

    def help_testing_options(self, logging_level, args):
        for level in args:
            self.assertTrue(self.set_level(level, logging_level))

    def test_set_critical_level(self):
        self.help_testing_options(logging.CRITICAL, ("critical", "crit", "c", "fatal"))

    def test_set_debug_level(self):
        self.help_testing_options(logging.DEBUG, ("debug", "dbg", "d"))

    def test_set_error_level(self):
        self.help_testing_options(logging.ERROR, ("error", "err", "e"))

    def test_set_info_level(self):
        self.help_testing_options(logging.INFO, ("info", "inf", "nfo", "i"))

    def test_set_warn_level(self):
        self.help_testing_options(logging.WARNING, ("warning", "warn", "w"))

    def test_set_invalid_level(self):
        with self.assertRaises(TypeError):
            self.log.level("trace")


def test_output():
    # All of these just need to output without errors.
    from zenlog import log
    log.debug("A quirky message only developers care about")
    log.info("Curious users might want to know this")
    log.warn("Something is wrong and any user should be informed")
    log.warning("Something is wrong and any user should be informed")
    log.error("Serious stuff, this is red for a reason")
    log.critical("OH NO everything is on fire")
    log.c("OH NO everything is on fire")
    log.crit("OH NO everything is on fire")


if __name__ == '__main__':
    unittest.main()
