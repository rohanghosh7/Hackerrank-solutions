def is_leap(year):
    leap = False
    if(year%4==0):
        if(year%100!=0 or year%400==0):
            return True
        else:
            return leap
    else:
        return leap

year = int(raw_input())
print is_leap(year)