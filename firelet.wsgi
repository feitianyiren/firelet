#!/usr/bin/env python
#
# Firelet WSGI launcher

os.chdir(os.path.dirname(__file__))

import bottle

# TODO: add imports here

application = bottle.default_app()
