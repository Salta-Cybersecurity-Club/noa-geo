"""Fixtures compartidas de tests."""

import pytest


@pytest.fixture
def salta_capital():
    return {"lat": -24.7829, "lon": -65.4232, "faja": 3}


@pytest.fixture
def api_token_doc():
    return "ign-example-token"
