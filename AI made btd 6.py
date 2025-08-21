import tkinter as tk
from tkinter import messagebox
import random
import time
import threading

class RacingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("1v1 Racing Game")
        self.window.resizable(False, False)

        # Canvas
        self.canvas = tk.Canvas(self.window, width=700, height=400, bg="black")
        self.canvas.pack()

        # Finish line
        self.finish_x = 650
        self.canvas.create_line(self.finish_x, 0, self.finish_x, 400, fill="white", dash=(5, 5))

        # Players
        self.player1 = self.canvas.create_rectangle(50, 120, 100, 170, fill="blue")
        self.player2 = self.canvas.create_rectangle(50, 230, 100, 280, fill="red")

        # Scoreboard
        self.score1 = 0
        self.score2 = 0
        self.score_text = self.canvas.create_text(350, 30, text="Blue: 0 | Red: 0", fill="white", font=("Arial", 16))

        # Obstacles & boosts
        self.obstacles = []
        self.boosts = []
        self.create_items()

        # Controls
        self.keys_enabled = False
        self.window.bind("d", lambda e: self.move_car(self.player1, "Blue"))
        self.window.bind("<Right>", lambda e: self.move_car(self.player2, "Red"))

        # Start button
        self.start_btn = tk.Button(self.window, text="Start Race", command=self.start_race)
        self.start_btn.pack(pady=10)

        self.window.mainloop()

    def create_items(self):
        """Create random obstacles and boosts"""
        for _ in range(4):
            x = random.randint(200, self.finish_x - 50)
            y = random.choice([130, 240])
            self.obstacles.append(self.canvas.create_rectangle(x, y, x+30, y+30, fill="gray"))

        for _ in range(3):
            x = random.randint(200, self.finish_x - 50)
            y = random.choice([140, 250])
            self.boosts.append(self.canvas.create_oval(x, y, x+25, y+25, fill="yellow"))

    def start_race(self):
        """Countdown and enable race"""
        self.clear_positions()
        self.keys_enabled = False
        threading.Thread(target=self.countdown).start()

    def countdown(self):
        for i in range(3, 0, -1):
            self.canvas.itemconfig(self.score_text, text=f"🚦 {i}")
            time.sleep(1)
        self.canvas.itemconfig(self.score_text, text="🏁 GO!")
        time.sleep(0.5)
        self.update_score()
        self.keys_enabled = True

    def move_car(self, car, player):
        if not self.keys_enabled:
            return

        speed = 15
        self.canvas.move(car, speed, 0)
        x1, y1, x2, y2 = self.canvas.coords(car)

        # Check obstacles
        for obs in self.obstacles:
            ox1, oy1, ox2, oy2 = self.canvas.coords(obs)
            if x2 > ox1 and x1 < ox2 and y2 > oy1 and y1 < oy2:
                self.canvas.move(car, -30, 0)  # bounce back
                return

        # Check boosts
        for boost in self.boosts:
            bx1, by1, bx2, by2 = self.canvas.coords(boost)
            if x2 > bx1 and x1 < bx2 and y2 > by1 and y1 < by2:
                self.canvas.move(car, 40, 0)  # speed jump
                self.canvas.delete(boost)
                self.boosts.remove(boost)
                break

        # Check win
        if x2 >= self.finish_x:
            if player == "Blue":
                self.score1 += 1
            else:
                self.score2 += 1
            self.keys_enabled = False
            messagebox.showinfo("🏆 Race Over", f"{player} WINS!")
            self.update_score()
            self.clear_positions()

    def clear_positions(self):
        """Reset cars to start line"""
        self.canvas.coords(self.player1, 50, 120, 100, 170)
        self.canvas.coords(self.player2, 50, 230, 100, 280)

    def update_score(self):
        self.canvas.itemconfig(self.score_text, text=f"Blue: {self.score1} | Red: {self.score2}")


if __name__ == "__main__":
    RacingGame()
