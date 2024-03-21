# Battleship

The Phase 3 project of Brent, Raff, and Mike.

## File Structure

```
lib
   |- game.py
   |- grid.py
   |- main.py
```

Run `python lib/game.py` to start a new game.

## Classes

A `Game` instance is created to store game scores and move players through the their turns.

A `Grid` instance is created for both the player and the computer to store the state of their individual game boards.

## Project Phase 1

Computer sets 1x1 ship locations, player shoots and collects hits or misses

## Project Phase 2

MVP :
Ships = 3
Ship size 1x1

Computer sets ship’s location (random)
User sets their ships / x & y

SCORE DISPLAY:
Opponent ships: 3 of 3
My ships: 3 of 3

FIRE
User sets target/x and y
If ship in target
print(‘target hit’) / change grid square

Update Opponent ship count

Computer returns Fire
Random to start.

If Player ship count reaches zero
Print Game Over

If Opponent ship count reaches zero
Print Victory

## Project Phase 3

- Support multiple sizes of ships (1x3, 1x4, 1x5)
- Ships may be oriented on board horizontally or vertically
- Improve computer play logic
