"""Browser test for a real round and independent replay."""

import pytest
from playwright.sync_api import expect

import app as web


@pytest.mark.e2e
def test_round_and_replay(page, live_server, monkeypatch):
    """Play a winning round, then a losing round with real rules."""
    monkeypatch.setattr(web.random, "choice", lambda moves: "rock")

    page.goto(live_server)
    page.get_by_role("button", name="Paper", exact=True).click()

    choices = page.locator(".choice-value")
    expect(choices.nth(0)).to_contain_text("Paper")
    expect(choices.nth(1)).to_contain_text("Rock")
    expect(page.locator(".result")).to_have_attribute("data-outcome", "win")
    expect(page.get_by_role("heading", name="You win!", exact=True)).to_be_visible()

    page.get_by_role("button", name="Scissors", exact=True).click()

    expect(choices.nth(0)).to_contain_text("Scissors")
    expect(choices.nth(1)).to_contain_text("Rock")
    expect(page.locator(".result")).to_have_attribute("data-outcome", "lose")
    expect(
        page.get_by_role("heading", name="Computer wins", exact=True)
    ).to_be_visible()
