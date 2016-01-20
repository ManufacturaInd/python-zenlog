import zenlog
import logging


def test_setlevel():
    log = zenlog.Log()
    log.level('info')
    assert log.level() == logging.INFO
    log.level('warn')
    assert log.level() == logging.WARNING


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
