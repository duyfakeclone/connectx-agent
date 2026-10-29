# ConnectX Agent

A ConnectX game-playing agent implemented in Python using minimax search and alpha-beta pruning.

## Features

- Minimax decision-making
- Alpha-beta pruning
- Center-first move ordering
- Precomputed winning windows
- Heuristic board evaluation

## Requirements

- Python 3.11+
- NumPy
- `kaggle-environments` for local evaluation

## Usage

Import `my_agent` from `agent.py` and pass it to a compatible ConnectX environment.

## Notes

Search depth affects both playing strength and execution time. Benchmark the agent under the target runtime limit before increasing the search depth.
