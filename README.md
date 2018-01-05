<h1 align="center">Snake Game</h1>
<p><em>This document provides general information on the Snake Game application.</em></p>


Why Snake Game
-------------

<p>The snake game is an arcade game and it has very simple logic.
It is an ideal example to demonstrate how to build games with Pygame.</p>
How it Works
------------
<table layout="fixed">
  <tr>
    <td>
      <p>Install python3 and pygame modules and run snakegame.py from terminal.</p>
    </td>
    <td>
      <img src="/src/images/readme1.png" max-height="240px" witdh="auto">
    </td>
  </tr>
  <tr>
    <td>
      <p>The player is represented as snake, which grows if it eats an apple. The goal of the game is to eat as many apples
          as possible without colliding into yourself.  This is very easy in the early phase of the game but is increasingly
          more difficult as the length of the snake grows.</p>
    </td>
    <td>
      <img src="/src/images/readme2.png" max-height="240px" witdh="auto">
    </td>
  </tr>
  <tr>
    <td>
      <p>When collides with itself or wall, game is over and it shows total score.</p>
    </td>
    <td>
      <img src="/src/images/readme3.png" max-height="240px" witdh="auto">
    </td>
  </tr>
    
</table>


Technology 
------------
This application was built using Python, Pygame, Py2app.  

For local use
--------

```bash
# Clone repository
git clone https://github.com/giri68/roommate-finder-client.git

# Change directory
cd snakeGame

# Installdependencies
install python3 and pygame

# Start the game
python3 snakegame.py
```
