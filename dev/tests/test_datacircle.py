"""Live tests: each makes real calls to https://api.datacircle.dev/v1, with no key."""

import importlib.util
import json
from pathlib import Path

_spec = importlib.util.spec_from_file_location("datacircle", Path(__file__).parents[2] / "helpers" / "datacircle.py")
datacircle = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(datacircle)


def _call(function, **args):
    return json.loads(function(args))


def test_list_apis_finds_an_api_by_its_words():
    answer = _call(datacircle.list_apis, query="email finder", limit=3)
    assert answer["apis"][0]["slug"] == "email-finder"
    assert len(answer["apis"]) <= 3


def test_best_plans_ranks_best_first():
    answer = _call(datacircle.best_plans, slug="Email Finder", limit=3)
    ranks = [plan["rank"] for plan in answer["plans"]]
    assert ranks == sorted(ranks) and len(ranks) == 3
    assert answer["plans"][0]["page"].startswith("https://datacircle.dev/")


def test_best_plans_names_the_slugs_when_one_is_wrong():
    answer = _call(datacircle.best_plans, slug="no-such-api")
    assert "error" in answer and "email-finder" in answer["error"]


def test_search_plans_by_price():
    answer = _call(datacircle.search_plans, api="email-finder", sort="price", limit=5)
    prices = [plan["perThousand"] for plan in answer["plans"] if "perThousand" in plan]
    assert answer["total"] > 5 and prices == sorted(prices)


def test_provider_by_its_name():
    answer = _call(datacircle.provider, slug="Bright Data")
    assert answer["slug"] == "bright-data" and answer["apis"]
