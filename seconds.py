# Prompts user for a time in seconds, then converts to hours minutes and seconds.
# 86400 seconds in a day

usersecondsinput = int(input("How many seconds? "))

minutes = usersecondsinput / 60
seconds = usersecondsinput % 60
hours = 0

# for each time minutes is over 60
while True:
    if minutes >= 60:
        hours = hours + 1
        minutes = minutes - 60
    else: # print result
        print(f"""
        You input:                         That is
        {int(usersecondsinput)} seconds.        {int(hours)} hour(s), {int(minutes)} minute(s) and {int(seconds)} second(s).
        """)
        break;

