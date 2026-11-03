"""An endless spiral journey with the Sun and eight planets, using Turtle.

Run: python sun_and_planets.py
Space: pause/resume | Up/Down: change speed | Escape: close
Sizes, distances, and speeds are artistic rather than to scale.
"""

import math
import random
import time
import turtle


WIDTH, HEIGHT = 1160, 860
ORBIT_TILT = 0.66
BACKGROUND = "#030712"
TRAVEL_SPEED = 170  # World units per second; the camera follows the Sun.
TRAIL_SECONDS = 5.5
TRAIL_STEPS = 100

# Name, orbit radius, planet diameter, color, radians per second.
PLANETS = [
    ("Mercury", 64, 7, "#b5a79a", 1.65),
    ("Venus", 97, 13, "#ecc488", 1.18),
    ("Earth", 135, 16, "#489dff", 0.86),
    ("Mars", 177, 11, "#e47b57", 0.67),
    ("Jupiter", 232, 33, "#dcb28b", 0.40),
    ("Saturn", 289, 27, "#e6ce91", 0.29),
    ("Uranus", 344, 21, "#8cdddd", 0.21),
    ("Neptune", 399, 20, "#5878ef", 0.16),
]


def make_pen():
    pen = turtle.Turtle(visible=False)
    pen.speed(0)
    pen.penup()
    return pen


def sun_position(elapsed):
    """Fly forward forever while making a corkscrew through 3D space."""
    return (TRAVEL_SPEED * elapsed,
            55 * math.cos(elapsed * 1.2),
            55 * math.sin(elapsed * 1.2))


def planet_position(index, elapsed):
    """Orbit the moving Sun in a plane across its direction of travel."""
    _, radius, _, _, orbit_speed = PLANETS[index]
    x, y, z = sun_position(elapsed)
    angle = elapsed * (0.9 + orbit_speed * 1.8) + index * 2.4
    return x, y + radius * math.cos(angle), z + radius * math.sin(angle)


def project_position(position, camera_x):
    """An angled side view makes the planets' helical paths visible."""
    x, y, z = position
    return 220 + (x - camera_x) * 0.8 + z * 0.45, y * ORBIT_TILT


def faded_color(color, brightness):
    channels = [int(color[index:index + 2], 16) for index in (1, 3, 5)]
    return "#" + "".join(f"{int(channel * brightness):02x}" for channel in channels)


def draw_trail(pen, position_at, elapsed, camera_x, color, width=1):
    # Reconstruct a fixed amount of history; no growing lists or canvas trails.
    pen.pensize(width)
    drawing = False
    last_band = None
    colors = [faded_color(color, level) for level in (0.15, 0.30, 0.50, 0.75)]
    for step in range(TRAIL_STEPS + 1):
        progress = step / TRAIL_STEPS
        sample_time = elapsed - TRAIL_SECONDS * (1 - progress)
        x, y = project_position(position_at(sample_time), camera_x)
        if not (-WIDTH / 2 + 5 < x < WIDTH / 2 - 5 and -310 < y < 315):
            pen.penup()
            drawing = False
            continue
        # Four brightness bands fade old portions into the darkness.
        band = min(3, int(progress * 4))
        if band != last_band:
            pen.color(colors[band])
            last_band = band
        pen.goto(x, y)
        if not drawing:
            pen.pendown()
            drawing = True
    pen.penup()


def orbit_position(center, radius, angle):
    return (center[0] + radius * math.cos(angle),
            center[1] + radius * math.sin(angle) * ORBIT_TILT)


def ellipse(pen, center, radius, tilt, color, width=1, start=0, stop=math.tau):
    pen.color(color)
    pen.pensize(width)
    steps = 72
    for step in range(steps + 1):
        angle = start + (stop - start) * step / steps
        pen.goto(center[0] + radius * math.cos(angle),
                 center[1] + radius * math.sin(angle) * tilt)
        if step == 0:
            pen.pendown()
    pen.penup()


def draw_sun(pen, center, elapsed):
    pen.goto(*center)
    pulse = 3 * math.sin(elapsed * 2.5)
    for diameter, color in [(104, "#111222"), (88, "#292025"),
                            (76, "#663724"), (66, "#e17b28")]:
        pen.dot(diameter + pulse, color)

    # Rotating short rays and nested discs give the Sun a warm, lively glow.
    pen.color("#e7a83e")
    pen.pensize(2)
    for index in range(12):
        angle = elapsed * 0.15 + index * math.tau / 12
        inner = 35 + pulse / 2
        outer = inner + 6 + 2 * math.sin(elapsed * 3 + index)
        pen.goto(center[0] + inner * math.cos(angle),
                 center[1] + inner * math.sin(angle))
        pen.pendown()
        pen.goto(center[0] + outer * math.cos(angle),
                 center[1] + outer * math.sin(angle))
        pen.penup()

    pen.goto(*center)
    pen.dot(59, "#ffb83e")
    pen.dot(49, "#ffd65c")
    pen.goto(center[0] - 8, center[1] + 9)
    pen.dot(24, "#ffe895")


def draw_planet(pen, planet, position, elapsed):
    name, _, size, color, _ = planet
    if name == "Saturn":
        ellipse(pen, position, 25, 0.32, "#a58f69", width=3)

    pen.goto(*position)
    pen.dot(size, color)
    pen.goto(position[0] - size * 0.18, position[1] + size * 0.18)
    pen.dot(max(2, size * 0.25), "#e5efff")

    if name == "Earth":
        pen.goto(position[0] + 2, position[1] + 1)
        pen.dot(5, "#6dc58a")
        moon = orbit_position(position, 19, elapsed * 2.8)
        pen.goto(*moon)
        pen.dot(4, "#d4dbe9")
    elif name == "Jupiter":
        pen.goto(position[0] + 6, position[1] - 5)
        pen.dot(7, "#b9795a")
    elif name == "Saturn":
        ellipse(pen, position, 25, 0.32, "#ead6a4", width=3,
                start=math.pi, stop=math.tau)

    pen.goto(position[0], position[1] - size / 2 - 17)
    pen.color("#b9c8e0")
    pen.write(name, align="center", font=("Arial", 9, "normal"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Infinite Spiral Flight | Python Turtle")
    screen.bgcolor(BACKGROUND)
    screen.tracer(0)

    stars = make_pen()
    trails = make_pen()
    bodies = make_pen()
    labels = make_pen()
    status = make_pen()

    # Wrapping stars provide endless space with several layers of parallax.
    star_field = [(random.uniform(-WIDTH / 2, WIDTH / 2),
                   random.uniform(-310, 315), random.uniform(0.3, 1.4))
                  for _ in range(135)]

    def draw_stars(elapsed):
        stars.clear()
        for start_x, y, depth in star_field:
            x = (start_x - elapsed * TRAVEL_SPEED * depth + WIDTH / 2) % WIDTH
            x -= WIDTH / 2
            stars.color("#34445e" if depth < 0.8 else "#839dc3")
            stars.pensize(1 if depth < 0.8 else 2)
            stars.goto(x, y)
            stars.pendown()
            stars.goto(min(WIDTH / 2, x + 4 + depth * 9), y)
            stars.penup()

    labels.goto(0, 365)
    labels.color("#e6efff")
    labels.write("I N F I N I T E   S P I R A L   F L I G H T", align="center",
                 font=("Arial", 20, "bold"))
    labels.goto(0, 338)
    labels.color("#7e96b9")
    labels.write("Racing through endless space, with eight worlds spiraling along.",
                 align="center", font=("Arial", 11, "normal"))
    labels.goto(0, -365)
    labels.write("SPACE  pause / resume     UP / DOWN  speed     ESC  exit",
                 align="center", font=("Arial", 11, "normal"))
    labels.goto(0, -390)
    labels.write("Camera follows the Sun. Artistic paths, sizes and speeds; not to scale.",
                 align="center", font=("Arial", 9, "normal"))

    elapsed = 0.0
    last_frame = time.perf_counter()
    paused = False
    running = True
    speed = 1.0

    def update_status():
        status.clear()
        status.goto(0, -337)
        status.color("#f5ce7a")
        state = "PAUSED" if paused else "SPIRAL FLIGHT"
        status.write(f"{state}   |   Speed {speed:.2f}x", align="center",
                     font=("Arial", 10, "bold"))

    def toggle_pause():
        nonlocal paused
        paused = not paused
        update_status()

    def change_speed(factor):
        nonlocal speed
        speed = max(0.25, min(4.0, speed * factor))
        update_status()

    def close():
        nonlocal running
        running = False
        screen.bye()

    def animate():
        nonlocal elapsed, last_frame
        if not running:
            return
        now = time.perf_counter()
        dt = min(now - last_frame, 0.05)
        last_frame = now

        if not paused:
            elapsed += dt * speed
            camera_x = TRAVEL_SPEED * elapsed
            center = project_position(sun_position(elapsed), camera_x)
            draw_stars(elapsed)
            trails.clear()
            bodies.clear()

            draw_trail(trails, sun_position, elapsed, camera_x, "#ffc34d", width=3)
            for index, planet in enumerate(PLANETS):
                draw_trail(trails, lambda t, i=index: planet_position(i, t),
                           elapsed, camera_x, planet[3])

            # Draw distant objects first so near planets cross in front of the Sun.
            objects = [(sun_position(elapsed)[2], None, center)]
            for index, planet in enumerate(PLANETS):
                world_position = planet_position(index, elapsed)
                position = project_position(world_position, camera_x)
                objects.append((world_position[2], planet, position))

            for _, planet, position in sorted(objects, key=lambda item: item[0],
                                               reverse=True):
                if planet is None:
                    draw_sun(bodies, center, elapsed)
                else:
                    draw_planet(bodies, planet, position, elapsed)

        screen.update()
        if running:
            screen.ontimer(animate, 20)

    screen.onkey(toggle_pause, "space")
    screen.onkey(lambda: change_speed(2), "Up")
    screen.onkey(lambda: change_speed(0.5), "Down")
    screen.onkey(close, "Escape")
    screen.listen()
    update_status()
    animate()
    screen.mainloop()


if __name__ == "__main__":
    try:
        main()
    except turtle.Terminator:
        pass
