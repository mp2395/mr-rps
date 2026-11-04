"""Tests for the winner rules and a submitted round."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.unit
@pytest.mark.parametrize(
    ("player", "computer", "expected"),
    [
        ("rock", "rock", "tie"),
        ("rock", "paper", "lose"),
        ("rock", "scissors", "win"),
        ("paper", "rock", "win"),
        ("paper", "paper", "tie"),
        ("paper", "scissors", "lose"),
        ("scissors", "rock", "lose"),
        ("scissors", "paper", "win"),
        ("scissors", "scissors", "tie"),
    ],
)
def test_nine_outcomes(player, computer, expected):
    """Check each matchup against its literal expected result."""
    assert determine_winner(player, computer) == expected


@pytest.mark.integration
def test_submitted_losing_round(monkeypatch):
    """Submit Rock against computer Paper using the real rules."""
    monkeypatch.setattr(web.random, "choice", lambda moves: "paper")

    with web.app.test_client() as client:
        response = client.post("/", data={"move": "rock"})

    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert "You chose" in html
    assert "Computer chose" in html
    assert "Rock" in html
    assert "Paper" in html
    assert 'data-outcome="lose"' in html
    assert "Computer wins" in html
    assert "Starter: game rules not built yet." not in html
