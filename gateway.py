# gateway.py
# Created by Jonathan Astacio and Vek Unbound
# Copyright © 2025. All Rights Reserved.

import os

class SMSGateway:
    def __init__(self):
        self.gateway_map = {
            "att": "@txt.att.net",
            "verizon": "@vtext.com",
            "tmobile": "@tmomail.net",
            "sprint": "@messaging.sprintpcs.com",
            "boost": "@myboostmobile.com",
            "cricket": "@sms.cricketwireless.net",
            "uscellular": "@email.uscc.net",
            "virgin": "@vmobl.com",
            "metropcs": "@mymetropcs.com",
            "googlefi": "@msg.fi.google.com"
        }

    def get_gateway_address(self, number, carrier):
        carrier = carrier.lower()
        if carrier in self.gateway_map:
            return f"{number}{self.gateway_map[carrier]}"
        raise ValueError(f"Unsupported carrier: {carrier}")
