# Project Statement

## Project Title
Game Performance Analyzer

## Problem Statement

Game performance can vary depending on the hardware, game and graphics settings being used. A user may have FPS results from a game but still find it difficult to compare different graphics settings and decide which setting is suitable for their system.

The Game Performance Analyzer is a command-line Python program designed to make this comparison simpler. The user enters their CPU, GPU, RAM, game configuration and FPS results for different graphics settings. The program then calculates FPS stability and a performance score, compares the tested settings and gives a basic graphics recommendation.

The project also contains local reference information for selected CPUs, GPUs and games. This allows the program to provide a simple hardware capability result without requiring an internet connection or an external service.

## Main Objectives

- Accept basic hardware and game information from the user.
- Store reference information for supported CPUs, GPUs and games.
- Accept FPS benchmark results for Low, Medium, High and Ultra settings.
- Calculate FPS stability and an overall performance score.
- Compare the results of different graphics settings.
- Provide a basic recommendation based on the target FPS.
- Generate a readable performance report.

## Scope and Limitation

The program does not automatically measure FPS or hardware utilisation. Benchmark values are entered by the user, and the bottleneck result is a rule-based indication based on those inputs. The hardware capability information is based on the local reference data included with the project.
