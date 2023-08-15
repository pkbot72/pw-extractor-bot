#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6460355965:AAGckDSYKkrY6tPRxGrkrWLLmGz0YHKCN2U")
    API_ID = int(os.environ.get("API_ID", "9741228"))
    API_HASH = os.environ.get("API_HASH", "6f339e8fa827a5147fa2ff03898d610c")
    AUTH_USERS = "809150135"


