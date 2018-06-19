__version__ = "1.11.5"
__pypi_username__ = "paypal"
__pypi_packagename__ = "paypalrestsdk"
__github_username__ = "paypal"
__github_reponame__ = "PayPal-Python-SDK"
__endpoint_map__ = {
    "live": "https://api.paypal.com",
    "sandbox": "https://api.sandbox.paypal.com",
    # PayPal sandbox endpoint that will only support acceptable TLS version
    "security-test-sandbox": "https://test-api.sandbox.paypal.com/"
}
__default_timeout__ = 300
