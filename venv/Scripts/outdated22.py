months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date = input("Date: ").strip()
    if date[0].isnumeric(): # format 1
        M, D, Y = [int(i) for i in date.split("/")]
        if M < 13 and D < 32:  # check date[0] <= 12 and date[1] <= 31 ### if not reprompt
            print(f"{Y}-{M:02}-{D:02}")
            break
        else:
            pass
    else:
        date = date.replace(",","").split() # format 2
        if date[0] in months: # check date[0] in months
            date[0] = months.index(date[0]) + 1
            M, D, Y = [int(i) for i in date]
            if D < 32:  # and date[1] <= 31 ### if not reprompt
                print(f"{Y}-{M:02}-{D:02}")
                break
            else:
                pass
        else:
            pass



# while True:
#     try:
#         date = input("Date: ")
#     else:

#         break



# IF ALL GOOD
    # IF format is M/D/YYYY
        # split list n save as int M D Y
        # print f Y-{M:02}-{D:02}
    # IF format is Month D, YYYY
        # remove "," split at space
        # save list elements as M = months.index(datesplit[0]) + 1
                            # int D Y
        # print f Y-{M:02}-{D:02}




# get input
# check if format is -- M/D/YYYY -- or -- Month D, YYYY --
