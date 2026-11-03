"""Animated black hole with Python Turtle.

Run: python lesson20.py
Space: pause / resume.  Escape: close the window.
This is an artistic visualization, not a physics simulation.
"""

import math
import random
import time
import turtle


WIDTH = 1000
HEIGHT = 760
HORIZON = 86
DISK_TILT = 0.30
PARTICLE_COUNT = 150
BACKGROUND = "#03040d"


def make_pen():
    pen = turtle.Turtle(visible=False)
    pen.speed(0)
    pen.penup()
    return pen


def disk_position(radius, angle):
    """Project a circular orbit into a tilted ellipse."""
    return radius * math.cos(angle), radius * math.sin(angle) * DISK_TILT


def make_particle(outer_edge=False):
    return {
        "radius": random.uniform(285, 330) if outer_edge else random.uniform(105, 330),
        "angle": random.uniform(0, math.tau),
        "speed": random.uniform(0.8, 1.4),
        "size": random.uniform(1.3, 3.2),
    }


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("BLACK HOLE | Space: pause / resume | Esc: close")
    screen.bgcolor(BACKGROUND)
    screen.colormode(255)
    screen.tracer(0)

    stars = make_pen()
    glow = make_pen()
    rear_disk = make_pen()
    hole = make_pen()
    front_disk = make_pen()
    labels = make_pen()

    # The star field is drawn once; only the black hole is redrawn each frame.
    for _ in range(240):
        x = random.randint(-WIDTH // 2, WIDTH // 2)
        y = random.randint(-HEIGHT // 2, HEIGHT // 2)
        if (x / 375) ** 2 + (y / 180) ** 2 < 1:
            continue
        brightness = random.randint(65, 200)
        stars.goto(x, y)
        stars.dot(random.choice([1, 1, 2, 2, 3]),
                  (brightness, brightness, min(255, brightness + 30)))

    labels.color("#dce6ff")
    labels.goto(0, 295)
    labels.write("B L A C K   H O L E", align="center",
                 font=("Arial", 24, "bold"))
    labels.color("#74839f")
    labels.goto(0, 267)
    labels.write("Beyond the edge of light", align="center",
                 font=("Arial", 11, "normal"))
    labels.goto(0, -315)
    labels.write("SPACE  pause / resume     |     ESC  exit", align="center",
                 font=("Arial", 11, "normal"))

    particles = [make_particle() for _ in range(PARTICLE_COUNT)]
    paused = False
    running = True
    elapsed = 0.0
    last_frame = time.perf_counter()

    def toggle_pause():
        nonlocal paused
        paused = not paused

    def close():
        nonlocal running
        running = False
        screen.bye()

    def draw_streak(pen, particle, front):
        radius = particle["radius"]
        angle = particle["angle"]
        # Short curved trails make the rotation visible.
        for segment in range(4):
            tail_angle = angle - segment * 0.025
            x, y = disk_position(radius, tail_angle)
            if (y < 0) != front:
                continue
            # The front half of the disk is also hidden by the event horizon.
            if x * x + y * y < (HORIZON + 3) ** 2:
                continue
            heat = max(0.0, min(1.0, (330 - radius) / 225))
            fade = 1 - segment * 0.19
            color = (int(255 * fade), int((85 + 160 * heat) * fade),
                     int((20 + 165 * heat ** 3) * fade))
            pen.goto(x, y)
            pen.dot(particle["size"] * (1 - segment * 0.12), color)

    def animate():
        nonlocal elapsed, last_frame
        if not running:
            return
        now = time.perf_counter()
        dt = min(now - last_frame, 0.05)
        last_frame = now

        if not paused:
            elapsed += dt
            for pen in (glow, rear_disk, hole, front_disk):
                pen.clear()

            # Nested dark halos soften the transition into the star field.
            glow.goto(0, 0)
            for diameter, color in [(252, "#080714"), (232, "#110a1a"),
                                    (214, "#231020"), (198, "#49202a")]:
                glow.dot(diameter, color)

            # A faint continuous disk sits underneath the moving material.
            for radius in (116, 145, 180, 225, 275, 320):
                rear_disk.color((40, 20, 24))
                rear_disk.pensize(1)
                rear_disk.goto(*disk_position(radius, 0))
                rear_disk.pendown()
                for step in range(1, 81):
                    rear_disk.goto(*disk_position(radius, step * math.tau / 80))
                rear_disk.penup()

            for particle in particles:
                radius = particle["radius"]
                particle["angle"] += dt * particle["speed"] * (210 / radius) ** 1.5
                particle["radius"] -= dt * (7 + 15 * (110 / radius))
                if particle["radius"] < 103:
                    particle.update(make_particle(outer_edge=True))
                draw_streak(rear_disk, particle, front=False)

            # The photon ring surrounds a completely black event horizon.
            hole.goto(0, 0)
            pulse = 1.5 * math.sin(elapsed * 2)
            hole.dot(193 + pulse, "#a84e32")
            hole.dot(185 + pulse, "#ffae61")
            hole.dot(179 + pulse, "#fff0bf")
            hole.dot(HORIZON * 2, "#000000")

            for particle in particles:
                draw_streak(front_disk, particle, front=True)

            # A few bright sparks race around the rim.
            for index in range(8):
                angle = elapsed * 1.8 + index * math.tau / 8
                front_disk.goto(90 * math.cos(angle), 90 * math.sin(angle))
                front_disk.dot(2, "#fff6dd")

        screen.update()
        if running:
            screen.ontimer(animate, 20)

    screen.onkey(toggle_pause, "space")
    screen.onkey(close, "Escape")
    screen.listen()
    animate()
    screen.mainloop()


if __name__ == "__main__":
    try:
        main()
    except turtle.Terminator:
        # Closing the window can interrupt a Turtle drawing command.
        pass



