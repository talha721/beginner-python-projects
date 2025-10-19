# BlackJack Game

A simple command-line Blackjack (21) game.

This README contains the game description, complete rules, how to play, how to run the game, and other useful information for contributors.

---

## Table of contents

- [Description](#description)
- [Objective](#objective)
- [Card values](#card-values)
- [Gameplay rules](#gameplay-rules)
- [Winning and payouts](#winning-and-payouts)
- [How to play (CLI)](#how-to-play-cli)
- [Installation & Running](#installation--running)
- [Notes about this implementation](#notes-about-this-implementation)
- [Contributing](#contributing)
- [License](#license)

---

## Description

Blackjack (also called 21) is one of the most popular casino card games. Players compete against the dealer to get a hand value as close to 21 as possible without going over. This project contains a small Python implementation intended to be run in a terminal.

## Objective

The objective of Blackjack is to beat the dealer by:
- Getting a hand value higher than the dealer's without exceeding 21 (busting), or
- Letting the dealer draw until they bust (go over 21), or
- Having a Blackjack (an ace and a 10-value card) when the dealer does not.

## Card values

- Number cards (2 through 10) are worth their face value.
- Face cards (Jack, Queen, King) are worth 10.
- Ace can be worth 1 or 11 — whichever makes the best hand without causing a bust.

## Gameplay rules

Below are the standard rules used for this README. The actual game implementation in `main.py` may or may not implement every optional rule — see "Notes about this implementation".

1. The dealer and player are each dealt two cards.
   - The player's cards are usually both face-up.
   - The dealer typically has one card face-up (the "upcard") and one face-down (the "hole card").

2. Blackjack (natural): If the player's first two cards are an Ace and a 10-value card, that's a Blackjack. A Blackjack normally beats any dealer hand except a dealer Blackjack, and is usually paid 3:2.

3. Player turn:
   - Hit: take another card.
   - Stand: take no more cards and end your turn.
   - Double Down (optional rule): double the initial bet, take exactly one more card, and then automatically stand.
   - Split (optional rule): if the first two cards are the same rank, they may be split into two separate hands with a second bet equal to the first. Each hand is played independently.
   - Surrender (optional rule): give up half the bet and end the hand immediately.

4. Dealer turn:
   - After the player finishes, the dealer reveals their hole card and draws according to fixed rules.
   - A common rule: dealer must hit until their hand totals 17 or more. Some casinos use "dealer hits on soft 17" (meaning the dealer draws if the total is 17 but includes an Ace counted as 11). Other casinos require the dealer to stand on all 17s.

5. Bust: If a hand exceeds 21, it busts and loses immediately.

6. Push (tie): If player and dealer have the same total (and neither busted), the result is a push — the player's bet is returned.

## Winning and payouts

- Blackjack (player) usually pays 3:2 (1.5x the bet) unless the dealer also has Blackjack (push).
- Regular win pays 1:1.
- Push returns the bet.
- Insurance (optional): If dealer's upcard is an Ace, players may take insurance — a side-bet up to half their original bet that pays 2:1 if the dealer has Blackjack. Insurance is generally a losing bet in the long run.

## How to play (CLI)

- Run the game using Python in the `projects/BlackJack Game` folder. Example:

  ```bash
  python main.py
  ```

  (On Windows using the default shell `cmd.exe`, the same command applies.)

- The CLI will prompt you for actions during the round (for example: `hit`, `stand`, `double`, `split` — depending on which actions are implemented in the current `main.py`).

- Follow the on-screen prompts to place bets and choose actions.

## Installation & Running

Requirements:
- Python 3.8 or newer (recommended).

Steps:
1. Open a terminal and change to the project directory:

   On Windows (cmd.exe):

   ```cmd
   cd "D:\Projects\Python\pythonCourse\projects\BlackJack Game"
   ```

2. Run the game:

   ```cmd
   python main.py
   ```

If `main.py` is not executable or empty, check the repository for an alternate runner or contact the project owner — this README provides generic instructions assuming a runnable `main.py` script is present.

## Notes about this implementation

- I inspected the `main.py` file in this folder and found it currently empty or containing no runnable code. Because of that, this README provides a complete set of game rules and instructions, but the behavior of the game depends on the actual `main.py` implementation.

- If you want the README to match the implemented feature set exactly (for example, whether `double`, `split`, or `insurance` are supported), either:
  - Paste the current `main.py` contents here, or
  - I can open and update `main.py` to a full playable Blackjack CLI implementation and then update the README to match the implemented features.

- Common optional features to consider adding to `main.py`:
  - Betting and bankroll across multiple rounds
  - Double down, split, surrender options
  - Multiple players
  - Deck shuffling and multiple decks
  - Basic logging of rounds and outcomes

## Contributing

Contributions are welcome. Please follow these steps:
1. Open an issue describing the feature or bug.
2. Create a branch for your change.
3. Submit a pull request with a clear description of changes and rationale.

If you'd like, I can implement additional features (a playable CLI, unit tests, or better documentation) — tell me which features you'd like and I will implement them.

## License

This folder does not currently include a license file. If you want to open-source this project, add a `LICENSE` file (MIT, Apache-2.0, etc.).

---

If you'd like, I can also:
- Implement a full playable `main.py` Blackjack CLI and wire the README to reflect exactly what the program supports.
- Create a small example game transcript and screenshot-ready sample output.

Tell me which of those you'd like next and I'll proceed.

