import math

# can cover information
can_cover_area = 5.1

# can size information
can_diameter = 0.15
can_height = 0.30

# box size information
box_length = 0.60
box_width = 0.30
box_height = 0.35

# calculations
room_area = 2 * ((40 * 3.4) + (30 * 3.4))

cans_in_boxes = (box_width // can_diameter) * (box_length // can_diameter) * (box_height // can_height)

number_of_cans = math.ceil(room_area / can_cover_area)

number_of_boxes = number_of_cans // cans_in_boxes

cans_left_over = number_of_cans % cans_in_boxes

# print results
print("There will be " + str(int(cans_in_boxes)) + " cans per box.")
print("There will be a total amount of " + str(int(number_of_cans)) + " cans.")
print("There will be a total amount of " + str(int(number_of_boxes)) + " boxes.")
print("There will be " + str(int(cans_left_over)) + " not in a box.")

