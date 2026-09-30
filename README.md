# Game Performance Analyzer

A Python-based console application that analyzes game performance using hardware information and FPS benchmark results entered by the user.

## Features

- Hardware configuration
- Game selection
- FPS performance recording
- FPS stability calculation
- Performance score and rating
- Rule-based bottleneck indication
- Graphics recommendation
- Console performance report
- Basic validation and testing
- Local CPU, GPU and game reference data using Python dictionaries

## Requirements

- Python 3.x
- Command-line / terminal
- No external Python packages are required

## Setup

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Check that Python is installed:

```bash
python --version
```

No `pip install` step is required because the project uses Python and its standard features only.

## Configuration / Reference Data

The file `database.py` contains the project's local reference data:

- `CPUS` - CPU information
- `GPUS` - GPU information
- `GAMES` - game information and target FPS

The data is stored as normal Python dictionaries, so it can be updated directly without using an external database or file format.

## How to Run

From the project root directory:

```bash
python main.py
```

The program asks for:

1. CPU, GPU and RAM
2. Game and resolution
3. FPS results for Low, Medium, High and Ultra
4. Benchmark duration

It then calculates stability and performance scores, compares the four settings, gives a graphics recommendation, and saves the result to `performance_report.txt`.

## Running Tests

Run:

```bash
python -m tests.test_analyzer
```

Expected output:

```text
All analyzer tests passed.
```

## Project Structure

```text
GamePerformance-Analyzer/
│
├── tests/
│   └── test_analyzer.py
│
├── database.py
├── analyzer.py
├── game.py
├── hardware.py
├── main.py
├── performance.py
├── recommender.py
├── report.py
├── README.md
└── .gitignore
```

## Important Design Note

The hardware reference data does not automatically detect the user's hardware. The program asks the user to enter CPU and GPU names and then searches the local Python dictionaries for matching information.

The FPS values are also entered by the user. The program does not automatically measure FPS or direct CPU/GPU utilization.

The bottleneck indications are rule-based estimates based on the entered benchmark information.
