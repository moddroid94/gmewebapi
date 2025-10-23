"""GME Web Api Wrapper"""

import logging
from typing import Any
import requests

_LOGGER = logging.getLogger()
_LOGGER.level = logging.DEBUG

DOMAIN = "https://www.mercatoelettrico.org"
HOME = "/it-it/Home"
HTTP_PATH = "/it-it/Home/Esiti/Elettricita/MGP/Esiti/"
PATH = "/DesktopModules/GmeEsitiPrezziME/API/item/GetMEPrezzi"
TOKEN_LENGTH = 71
TOKEN_OFFSET = 49

params = {
    "DataInizio": 0,
    "DataFine": 0,
    "Granularita": "",
    "Mercato": "",
    "Zona": "",
    "Tipologia": "",
}

headers = {
    "authority": DOMAIN,
    "method": "GET",
    "path": PATH,
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "moduleid": "530",
    "requestverificationtoken": "",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "tabid": "48",
}


class Timeframe:
    def __init__(self):
        self.hour = "h"
        self.halfhour = "hh"
        self.quarter = "qh"
        self.day = "d"
        self.month = "m"
        self.year = "y"


class Zone:
    def __init__(self):
        self.pun = "PUN"
        self.nord = "NORD"
        self.calabria = "CALA"
        self.centro_nord = "CNOR"
        self.centro_sud = "CSUD"
        self.sardegna = "SARD"
        self.sicilia = "SICI"
        self.sud = "SUD"
        self.italia = "NAT"


class Market:
    def __init__(self):
        self.mgp = "MGP"
        self.mi = "MI-A1"


class PriceType:
    def __init__(self):
        self.pun = "PUN"
        self.prezzi_zonali = "PrezziZonali"


class GME:
    def __init__(self):
        self.session = requests.Session()
        self.token = ""
        self.headers = {}

    def _get_token(self, req: requests.Response) -> str | None:
        offset = req.text.find("__RequestVerificationToken")
        if offset == -1:
            _LOGGER.error("No token string found in homepage")
            return None

        token_start = offset + TOKEN_OFFSET  # fixed offset to the start of token value
        token_end = token_start + TOKEN_LENGTH
        token = req.text[token_start:token_end]
        return token

    def _get_tabid(self, price_type: str) -> str | None:
        req = self.session.get(DOMAIN + HTTP_PATH + price_type)
        offset = req.text.find("sf_tabId")
        if offset == -1:
            _LOGGER.error("No tabid string found in homepage")
            return None

        tabid_start = offset + 11
        tabid_end = tabid_start + 2
        tabid = req.text[tabid_start:tabid_end]
        return str(tabid)

    def initialize(self) -> bool:
        req = self.session.get(DOMAIN + HOME)

        if req.status_code != 200:
            _LOGGER.error("Request error: %s", req.text)
            return False

        self.token = self._get_token(req)

        if self.token is None:
            _LOGGER.error("No Token Found")
            return False
        return True

    def getPrices(
        self,
        start=0,
        end=0,
        timeframe=Timeframe().hour,
        market=Market().mgp,
        zone=Zone().pun,
        price=PriceType().pun,
    ) -> Any | None:
        request_params = params
        request_params["DataInizio"] = start
        request_params["DataFine"] = end
        request_params["Granularita"] = timeframe
        request_params["Mercato"] = market
        request_params["Zona"] = zone
        request_params["Tipologia"] = price

        req = requests.Request(
            "GET", DOMAIN + PATH, headers=headers, params=request_params
        )
        prepped = self.session.prepare_request(req)
        prepped.headers["path"] = prepped.url
        prepped.headers["requestverificationtoken"] = self.token
        prepped.headers["tabid"] = self._get_tabid(price)

        res = self.session.send(prepped)
        if res.status_code != 200:
            _LOGGER.error("Errore Retrieving Data: %s", res.status_code)
            return None

        try:
            return res.json()
        except requests.exceptions.JSONDecodeError as e:
            _LOGGER.error("Not a valid JSON response. Error:%s. At: %s", e.msg, e.pos)
            return None

    def close(self):
        self.session.close()
        return
