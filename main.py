def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
        # print("Leap year.")
      else:
        return False
        # print("Not leap year.")
    else:
        return True
    #   print("Leap year.")
  else:
    return False
    # print("Not leap year.")

def days_in_month(iYear, iMonth):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  isLeapYear = is_leap(iYear)
  if isLeapYear and iMonth == 2:
      return month_days[1] + 1
  elif not isLeapYear and iMonth == 2:
      return month_days[1]
  else:
      return month_days[iMonth - 1]

  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












