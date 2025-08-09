from seleniumbase import SB
import time
import requests
import sys
import requests
import os
import random
import subprocess
from dataclasses import dataclass
from typing import List, Optional

import requests

def is_stream_online(username):
    """
    Returns True if the Twitch stream is online, False otherwise.
    Uses the public frontend Client-ID (no OAuth).
    """
    url = f"https://www.twitch.tv/{username}"
    headers = {
        "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko",  # Publicly known Client-ID
    }
    resp = requests.get(url, headers=headers)
    return "isLiveBroadcast" in resp.text

with SB(uc=True, test=True) as clibun:

    url = "https://kick.com/brutalles"
    clibun.uc_open_with_reconnect(url, 4)
    clibun.sleep(4)
    clibun.uc_gui_click_captcha()
    clibun.sleep(1)
    clibun.uc_gui_handle_captcha()
    clibun.sleep(4)
    if clibun.is_element_present('button:contains("Accept")'):
        clibun.uc_click('button:contains("Accept")', reconnect_time=4)
    if clibun.is_element_visible('#injected-channel-player'):
        clibun2 = clibun.get_new_driver(undetectable=True)
        clibun2.uc_open_with_reconnect(url, 5)
        clibun2.uc_gui_click_captcha()
        clibun2.uc_gui_handle_captcha()
        clibun.sleep(10)
        if clibun2.is_element_present('button:contains("Accept")'):
            clibun2.uc_click('button:contains("Accept")', reconnect_time=4)
        while clibun.is_element_visible('#injected-channel-player'):
            clibun.sleep(10)
        clibun.quit_extra_driver()
    clibun.sleep(1)
    if is_stream_online("brutalles"):
        url = "https://www.twitch.tv/brutalles"
        clibun.uc_open_with_reconnect(url, 5)
        if clibun.is_element_present('button:contains("Accept")'):
            clibun.uc_click('button:contains("Accept")', reconnect_time=4)
        if True:
            clibun2 = clibun.get_new_driver(undetectable=True)
            clibun2.uc_open_with_reconnect(url, 5)
            clibun.sleep(10)
            if clibun2.is_element_present('button:contains("Accept")'):
                clibun2.uc_click('button:contains("Accept")', reconnect_time=4)
            while clibun.is_element_visible(input_field):
                clibun.sleep(10)
            clibun.quit_extra_driver()
    clibun.sleep(1)

