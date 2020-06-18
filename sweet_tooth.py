starting_amount_of_sweets = 40
amount_of_students = 14

amount_remaining = starting_amount_of_sweets % amount_of_students
print("Remaining amount of sweets: " + str(amount_remaining))

used_sweets = starting_amount_of_sweets - amount_remaining

amount_each_got = used_sweets / amount_of_students

print("Each student got: " + str(amount_each_got) + " sweets")