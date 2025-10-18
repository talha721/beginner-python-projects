# Secret Auction

A small interactive command-line Python program that collects bids from multiple users and determines the highest bidder.

## Files

- `main.py` — the auction program. It prompts for bidder names and their bids, then prints the winner and the winning amount.

## How it works

1. The script asks each bidder for their name and bid (an integer).
2. Bids are stored in a dictionary with the bidder name as the key and the bid amount as the value.
3. When there are no more bidders, the script finds the highest bid and prints the winner.

## Usage

Open a terminal, change into the `Secret Auction` folder and run:

```bash
python main.py
```

Follow the prompts. Example session:

```
Welcome to the secret auction program.
What is your name?: Alice
What is your bid?: $50
Are there any other bidders? Type 'yes' or 'no'.
yes

What is your name?: Bob
What is your bid?: $75
Are there any other bidders? Type 'yes' or 'no'.
no
The winner is Bob with a bid of $75
```

## Notes and suggestions

- The current `main.py` converts input bids to integers; non-integer entries will raise an error. Consider adding input validation if you expect non-integer input.
- The script currently clears the screen by printing multiple newlines when another bidder joins; you may replace that with a proper terminal clear command if desired.

## License

This project is unlicensed. Feel free to use it for learning and modify as needed.

