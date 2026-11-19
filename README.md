# Simple AI Projects

A collection of small AI projects built with classic algorithms like minimax and with machine learning libraries like scikit-learn.

## Tech Stack

* **Core:** Python
* **Algorithms:** Minimax with alpha-beta pruning, genetic algorithm
* **Machine learning:** scikit-learn (see the `machine-learning` folder)
* **Database:** None

## Projects

| Project | Description |
| --- | --- |
| `connect-four.py` | Play Connect Four in the terminal against a computer opponent that uses minimax with alpha-beta pruning. |
| `tictactoe.py` | Tic-tac-toe against the computer. Uses regular minimax without alpha-beta pruning |
| `genetics-algorithm.py` | A genetic algorithm example. Tries to find a word represented by numbers |
| `machine-learning/` | Machine learning experiments using scikit-learn. Inside is a classification and regression example with Scikit-Learn & Kaggle datasets |

## Quick Start

Instructions to get the development environment running locally.

```bash
# Clone the repository
git clone https://github.com/JosaphatCornelius/simple-ai-projects.git
cd simple-ai-projects

# Run a project
python connect-four.py
```

*Note: Ensure you have Python 3 installed. The game scripts use only the standard library. The `machine-learning` projects need scikit-learn, so install it with `pip install scikit-learn`.*

## Usage

Run any script directly with Python. For example, to play Connect Four:

```bash
python connect-four.py
```

1. Choose `X` or `O`.
2. Choose whether you want to move first (`y` or `n`).
3. On your turn, enter a column number from 1 to 7 to drop your disc.

The first player to connect four discs in a row, column, or diagonal wins. The game also reports a draw when the board is full.

## Contributing & License

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License: none at the moment.
