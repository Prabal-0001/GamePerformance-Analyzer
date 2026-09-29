# Game Performance Analyzer

A simple Python project that checks game performance using hardware details and FPS results.

## What it does

- Takes CPU, GPU and RAM input
- Looks up the CPU and GPU in JSON files
- Selects a game and resolution
- Takes FPS results for Low, Medium, High and Ultra
- Compares the four settings
- Gives a basic hardware capability result
- Suggests a graphics setting based on target FPS
- Creates a text report

## How to run

Open a terminal in this folder and run:

```
python main.py
```

For the test file:

```
python -m tests.test_analyzer
```

## Files

- `main.py` - starts the program
- `hardware.py` - CPU/GPU input and database lookup
- `game.py` - game input
- `performance.py` - FPS input
- `analyzer.py` - calculations and comparison
- `recommender.py` - graphics recommendation
- `report.py` - prints and saves the report
- `data/` - CPU, GPU and game data
- `tests/` - simple tests

The final report is saved as `performance_report.txt`.
