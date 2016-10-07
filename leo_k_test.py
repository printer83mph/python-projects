import math

def horizontal_distance(angle,magnitude):
    vertical_velocity = math.sin(math.radians(angle))*magnitude
    horizontal_velocity = math.cos(math.radians(angle))*magnitude
    half_time = vertical_velocity/9.8
    full_time = half_time * 2
    return horizontal_velocity*full_time

print(horizontal_distance(float(input("Angle? (degrees)\n>>> ")),float(input("Magnitude? (m/s)\n>>> "))))
