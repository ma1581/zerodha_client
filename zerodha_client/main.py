from urllib.parse import urlparse, parse_qs

import pyotp
from playwright.sync_api import sync_playwright

from zerodha_client.libs.currency_utils import CurrencyUtils
from zerodha_client.models.dashboard import DashboardDetails


class ZerodhaClient:
    ZERODHA_COIN_LOGIN_URL = "https://coin.zerodha.com/login"
    ZERODHA_COIN_DASHBOARD_URL = "https://coin.zerodha.com/dashboard"

    def __init__(self, totp_auth_url, username, password):
        self.TOPT_AUTH_URL = totp_auth_url
        self.username = username
        self.password = password
        self._setup_playwright()

    def _setup_playwright(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.page = self.browser.new_page()

    def login(self):
        self.page.goto(self.ZERODHA_COIN_LOGIN_URL)
        self.page.wait_for_selector("#userid")
        self.page.fill("#userid", self.username)
        self.page.fill("#password", self.password)
        self.page.press("#password", "Enter")
        self.page.wait_for_load_state("networkidle")

        parsed_url = urlparse(self.TOPT_AUTH_URL)
        query_params = parse_qs(parsed_url.query)
        secret = query_params.get("secret", [None])[0]
        totp = pyotp.TOTP(secret)
        otp_code = totp.now()

        with self.page.expect_navigation():
            self.page.fill("#userid", otp_code)
            self.page.wait_for_load_state("networkidle")

    def get_dashboard_details(self):
        self.page.goto(url=self.ZERODHA_COIN_DASHBOARD_URL, wait_until="networkidle")
        mf_div = self.page.query_selector(".row.mf-row")
        mf_div_components = mf_div.query_selector_all(".three.columns")
        invest_div = mf_div_components[0]
        invest_amount = invest_div.query_selector("span").get_attribute("data-balloon")
        current_invest_div = mf_div_components[1]
        current_amount = current_invest_div.query_selector("span").get_attribute(
            "data-balloon"
        )
        return DashboardDetails(
            CurrencyUtils.format_currencies(invest_amount),
            CurrencyUtils.format_currencies(current_amount),
        )

    def close(self):
        self.browser.close()
        self.playwright.stop()
