log_file = open("um-server-01.txt")
# line 1 is declaring the variable "log_file" as the function open, which opens files in python. The function open is opening the file "um-server-01.txt"

def sales_reports(log_file):
#line 4 is defining a new function called sales_reports, which takes in one parameter: log_file.
    for line in log_file:
#line 6 is looping over the file line by line
        line = line.rstrip()
#line 8 is defining the variable line as line.rstrip(), meaning the line of code will be stripped of whatever's in the (), which in this case will be trailing whitespace
        day = line[0:3]
#line 10 is setting the variable day = line[0:3] which means that day = the first three letters in the line string
        if day == "Mon":
#line 12 is posing an if statement, if day == "Tue": which puts a conditional on the variable day
            print(line)
#line 14 is the outcome of the if statement above. the outcome is print(line) while will print out the value of the variable line into the console


sales_reports(log_file)
#line 18 is invoking the sales_reports function and calling the parameter(log_file), the outcome for this will show in the console, it's every day in the um-server-01.txt file that begins with the letters "Tue"

#the recall on this would be 100% percent because our function pulled all of the possible "tue" data possible 