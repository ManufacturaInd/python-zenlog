
Zenlog is a Python logging tool for lazy people, meant for quick use of 
prettified log messages.

It is a very light wrapper around 
[colorlog](https://github.com/borntyping/python-colorlog), a wonderful library
for color output in logging messages. In addition, Zenlog hides
the standard library logger hierarchy, using only the root logging
instance.

This won't fit many advanced uses, but it's good for quick scripts
that could use easy-to-read and clear log output with a dead simple
API.

Usage
-----

Don't want to stop to read the docs every time you want to have some
quick logging in a hacky script you're writing? Just one line and 
you're good to go:

    from zenlog import log

It should then be easy to get going:

    log.debug("A quirky message only developers care about")
    log.info("Curious users might want to know this")
    log.warn("Something is wrong and any user should be informed")
    log.error("Serious stuff, this is red for a reason")
    log.critical("OH NO everything is on fire")

Output:

![Zenlog output](http://manufacturaindependente.com/dump/zenlog1.png)

You can be as lazy as you want:

    log.crit("Abbreviations are fine")
    log.c("First letters also work")
    
A keystroke saved is a bone joint slightly spared! ;o)

Switching from the standard logging library
-------------------------------------------

It's straightforward to adapt to scripts that already make use 
of the standard logging library. Just change the line:

    import logging

to

    from zenlog import logging

And it should make your log messages more readable. There's many
important features missing -- see below.


Installation
------------

Also simple:

    pip install zenlog

Missing features
----------------

Important:

  * go beyond styling the errorlevel names, provide other
    variables like human timestamp, username, hostname...
  * datetime support and other useful log output
  * testing on any terminal other than uxterm
  * finer-grained color control
  * make it easy for any coder to change the theme to their style

Less-priority but also important:

  * "theme" support, emulating some used log schemes (Xorg, Gentoo...)
  * come up with a simpler template system for theming (a layer on top
    of the shell commands) -- a subset of CSS? See [term-css](https://www.npmjs.org/package/term-css) for the syntax
  * Use of fancy Unicode characters
  * Additional sets of levels other than debug, info, etc?
  * Always show line numbers on debug?
