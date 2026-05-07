# 🐍 Snake Game (Python / Pygame)

A classic Snake game built from scratch using **Python** and **Pygame**, with a focus on clean architecture, real-time game logic, and modular design.

---

## 🎮 Features

- Grid-based movement system  
- Timer-driven movement using Pygame events  
- Direction locking to prevent invalid reverse moves  
- Self-collision detection (game over logic)  
- Apple spawning with collision avoidance  
- Dynamic snake growth  
- Screen wrap-around movement  
- Modular code structure (Game, Snake, Screen, Settings)

---

## 🧠 Technical Highlights

- **Event-driven updates** using `pygame.time.set_timer()`  
- **Stable frame rate control** with `clock.tick()`  
- **Grid-based positioning** using configurable `CELL_SIZE`  
- **Collision detection** for both snake body and apple  
- **Clean rendering pipeline** with centralized draw logic  
- **Separation of concerns** across modules:
  - `game.py` → main loop & game logic  
  - `snake.py` → snake behavior & state  
  - `screen.py` → rendering layer  
  - `settings.py` → configuration & assets  

---

## ▶️ How to Run

🎯 Controls
⬆️ Up Arrow
⬇️ Down Arrow
⬅️ Left Arrow
➡️ Right Arrow

### 1. Install dependencies

```bash
pip install pygame

python game.py


