# Coffee Machine — Procedural vs OOP

I built this as part of my Python learning journey. The idea was to solve 
the same problem twice — once the "normal" way (procedural) and once using 
Object-Oriented Programming — to understand what OOP actually adds and why 
it exists.

## What it does

Simulates a coffee machine that:
- Takes orders (espresso, latte, cappuccino)
- Checks if resources are sufficient
- Processes coin payments and returns change
- Tracks remaining ingredients and profit
- Prints a report on demand

## Two approaches, same problem

**Procedural** (`coffee_machine_procedural.py`) — everything in functions, 
data stored in dictionaries, straightforward logic flow.

**OOP** (`coffee-machine-oop/`) — split into three classes: `Menu`, 
`CoffeeMaker`, and `MoneyMachine`. Each class owns its data and behaviour.

The procedural version was written first, completely from scratch. The OOP 
version came after — and the difference in how state is managed made the 
point of OOP click.

## Built with

Python 3 | No external libraries required

## How to run

```bash
# Procedural
python coffee_machine_procedural.py

# OOP
python coffee-machine-oop/main.py
```