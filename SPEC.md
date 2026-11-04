# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan
We will build one independent round using the supplied interface and server.
The winner function will return win, lose, or tie from the player's perspective.
Both choices and the result will appear. Choosing again starts a new round.
We will not add scoring, storage, accounts, frameworks, or AI APIs.

Prediction: Player Paper beats computer Rock because Paper covers Rock.
AI helped clarify the player's perspective during planning.
A valid losing round is player Rock against computer Paper, returning lose.
Missing input and unsupported input such as banana must return HTTP 400
with a helpful message.

We will add nine explicit unit outcomes, a real request/result integration
test, and a browser round with replay using the supplied fixtures.
Tests will use unit, integration, or e2e markers. Positive tests will control
only randomness. We will reuse the supplied negative checks, run the full
check.py, and review the code and tests against this plan.
### Checks

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.
### Work record

### Work record

- Issue: https://github.com/mp2395/mr-rps/issues/1
- Implementation: [Winner rules](game.py).
- Tests: [Unit and integration](tests/test_game.py) and
  [Browser round and replay](tests/e2e/test_round.py).
- Full local checks: `.venv/bin/python check.py` passed Black,
  Pylint, 23 non-browser tests, and 6 Chromium browser tests.
- Test reviewed with AI help: player Paper against computer Rock
  must return win. This catches an incorrect result for that matchup.
- Browser observation: I chose Rock, the computer chose Rock,
  and the result was a tie. This makes sense because both moves
  were the same. Clicking another move started a new round.
- - Manual keyboard controls: Tab/Option+Tab highlighted a move,
  and Enter played a new round successfully.
- Help received: ChatGPT helped with planning, code, tests,
  troubleshooting, and review. Local Copilot was attempted but
  did not produce usable responses; implementation help came
  through browser chat.
- - Pull request: https://github.com/mp2395/mr-rps/pull/2
- CI run: https://github.com/mp2395/mr-rps/actions/runs/41790838229
- Checks: **Rules not verified.** Supplied request/browser tests cover the shell only. After implementation, record actual full-check results and your browser observations here; put detailed results in the PR. Passing formatting and analysis alone is not evidence of correct rules.
