🐍 Snake Game (Python / Pygame)

A classic Snake game built from scratch using Python and Pygame, focusing on clean architecture, real-time game logic, and modular design.

🎮 Features

  Grid-based movement system
  Smooth, timer-driven game loop
  Direction locking to prevent invalid turns
  Self-collision detection (game over logic)
  Apple spawning with collision avoidance
  Dynamic snake growth
  Screen wrap-around movement
  Modular code structure (Game, Snake, Screen, Settings)

🧠 Technical Highlights

Event-driven movement using pygame.time.set_timer()
Frame rate control with clock.tick()
Separation of concerns:
  game.py → game loop & logic
  snake.py → snake state & behavior
  screen.py → rendering
  settings.py → configuration & assets
Grid system based on CELL_SIZE for consistent positioning
Optimized rendering pipeline (single draw call per frame)
