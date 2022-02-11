
def add_time(start, duration, *day):

    time =  findTime(start, duration)
    passday = passDay(start, duration)

    if len(day) == 0:
        result = time + " " + passday
        return result
    else:
        numDay = dayToNum(day[0])
        day = findDay(start, duration, numDay)
        result = time + ", " + numToDay(day) + passday
        return result
    
def findTime(start, duration):
    startspl = start.split()
    startspl2 = startspl[0].split(":")
    unit = startspl[1]
    startHr = int(startspl2[0])
    startMn = int(startspl2[1])

    durspl = duration.split(":")
    durHr = int(durspl[0])
    durMn = int(durspl[1])

    rsMn = startMn + durMn
    hfm = 0

    if rsMn >= 60:
        hfm += int(rsMn / 60)
        rsMn = rsMn % 60

    rsHr = startHr + durHr + hfm

    if rsHr >= 12:
        num = int(rsHr / 12)
        for i in range(num):
            if unit == "AM":
                unit = "PM"
            else: unit = "AM"
            rsHr = rsHr - 12

    if len(str(rsMn)) < 2:
        rsMn = str("0" + str(rsMn))
    
    result = str(rsHr) + ":" + str(rsMn) + " " + unit
    return result

def dayToNum(day):
    num = 0
    if day.lower() == "sunday":
        num = 1
    elif day.lower() == "monday":
        num = 2
    elif day.lower() == "tuesday":
        num = 3
    elif day.lower() == "wednesday":
        num = 4
    elif day.lower() == "thurday":
        num = 5
    elif day.lower() == "friday":
        num = 6
    elif day.lower() == "saturday":
        num = 7

    return num

def findDay(start, duration, day):
    startspl = start.split()
    startspl2 = startspl[0].split(":")
    unit = startspl[1]
    startHr = int(startspl2[0])
    startMn = int(startspl2[1])

    durspl = duration.split(":")
    durHr = int(durspl[0])
    durMn = int(durspl[1])

    rsMn = startMn + durMn
    hfm = 0

    if rsMn >= 60:
        hfm += int(rsMn / 60)
        rsMn = rsMn % 60

    rsHr = startHr + durHr + hfm

    c = 0
    count = 0

    if rsHr >= 12:
        if unit == "AM":
            num = int(rsHr / 12)
            for i in range(num):
                c += 1
            count = int(c/2)
        if unit == "PM":
            num = int(rsHr / 12)
            for i in range(num):
                c += 1
            count = int(c/2 + 0.5)
            
    days = day + count

    if days > 7:
        while days > 7:
            days = days - 7

    return days

def numToDay(num):
    day = ""
    if num == 1:
        day = "Sunday"
    elif num == 2:
        day = "Monday"
    elif num == 3:
        day = "Tuesday"
    elif num == 4:
        day = "Wednesday"
    elif num == 5:
        day = "Thurday"
    elif num == 6:
        day = "Friday"
    elif num == 7:
        day = "Saturday"

    return day

def passDay(start, duration):
    startspl = start.split()
    startspl2 = startspl[0].split(":")
    unit = startspl[1]
    startHr = int(startspl2[0])
    startMn = int(startspl2[1])

    durspl = duration.split(":")
    durHr = int(durspl[0])
    durMn = int(durspl[1])

    rsMn = startMn + durMn
    hfm = 0

    if rsMn >= 60:
        hfm += int(rsMn / 60)
        rsMn = rsMn % 60

    rsHr = startHr + durHr + hfm

    c = 0
    count = 0

    if rsHr >= 12:
        if unit == "AM":
            num = int(rsHr / 12)
            for i in range(num):
                c += 1
            count = int(c/2)
        if unit == "PM":
            num = int(rsHr / 12)
            for i in range(num):
                c += 1
            count = int(c/2 + 0.5)
    
    if count == 0:
        return ""

    if count == 1:
        return "(" + "next day" + ")"

    if count > 1:
        return "(" + str(count) +" days later" + ")"