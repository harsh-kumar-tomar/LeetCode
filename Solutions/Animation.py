from math import sin, cos  # Use math, not cmath
from vpython import sphere, vector, color, rate, scene

# Set up the top view
scene.camera.pos = vector(0, 50, 0)  # Camera placed above the scene
scene.camera.axis = vector(0, -50, 0)  # Point the camera downward
scene.background = color.black  # Optional: black background for better visibility

# Sun and planets' properties
sun = sphere(pos=vector(0, 0, 0), radius=1, color=color.yellow)

planets = [
    {"name": "Mercury", "color": color.gray(0.5), "radius": 0.2, "orbit_radius": 4, "speed": 0.05},
    {"name": "Venus", "color": color.orange, "radius": 0.3, "orbit_radius": 6, "speed": 0.03},
    {"name": "Earth", "color": color.blue, "radius": 0.4, "orbit_radius": 8, "speed": 0.02},
    {"name": "Mars", "color": color.red, "radius": 0.35, "orbit_radius": 10, "speed": 0.015},
]

# Create planet spheres
for planet in planets:
    planet["sphere"] = sphere(
        pos=vector(planet["orbit_radius"], 0, 0),
        radius=planet["radius"],
        color=planet["color"],
        make_trail=True,
    )
    planet["angle"] = 0  # Initial angle in radians

# Animation loop
while True:
    rate(120)  # 60 frames per second
    for planet in planets:
        # Update position using circular motion equations
        planet["angle"] += planet["speed"]
        x = planet["orbit_radius"] * cos(planet["angle"])
        z = planet["orbit_radius"] * sin(planet["angle"])
        planet["sphere"].pos = vector(x, 0, z)  # Update planet position
