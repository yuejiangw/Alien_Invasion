# Alien Invasion

A 2D game based on Pygame. You will control a spacecraft to defend against the alien attack.

Dependencies: Python 3.6.3 + Pygame 1.9.4

## GUI Design

* The window size is of 1300 * 700, with full screen display.
* The top right corner of the window shows the player's current score and current level respectively.
* The highest ever record is directly above the screen.
* The top left corner shows the remaining game opportunities.
* The middle of the window are the aliens, which will keep moving left and right.
* The bottom is the player-controlled spaceship, which can move horizontally.

## Control

* Use the following command to execute the `alien_invasion.py` file, enter the game.
  ```shell
  python alien_invasion.py
  ```
* Press button `Play` to start the game.
* Press `Q` to exit the game whenever you want.
* Use `A`, `D` or `←`, `→` to move the spacecraft.
* Use `Space` to shoot.

## Rules

* There can only be a maximum of three flying bullets on the screen at the same time, so you have to find the right time to fire.
* When all the aliens on the screen are eliminated, the difficulty level will increase by one, and the overall speed of the game will be accelerated and the score will be higher.
* When the ship collides with the alien or the alien reaches the bottom line of the screen, you lose one chance, and the game ends when the remaining chance is 0.

