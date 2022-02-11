from time_calculator import add_time

def inputTime():
	# ask for start time
	time = input("What is your time? (input look like: 1:05): ")
	AMPM = input("\nAM or PM (a/p): ")

	if AMPM.lower() == "p":
		AMPM = "PM"
	else: AMPM = "AM"
	start = time + " " + AMPM
	
	print("\nThis is your start time: " + start + "\n----------------------------------------")

	# ask for add time
	duration = input("How much do you add time? (input look like: 5:55): ")

	# ask want day
	q = input("Do you want day in outcome? (y/n): ")

	if q.lower() == "y":
		print(askDay(start, duration))
	else: print("----------------------------------------\n" + add_time(start, duration))

def askDay(start, duration):
	day = input("What is day in start day (input look like: Tuesday): ")
	print("\n----------------------------------------")
	result = add_time(start, duration, day)
	return result
	
inputTime()

# print(add_time("11:59 AM", "0:01", "tuesDaY"))