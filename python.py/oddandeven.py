# start=int(input("Enter the first number:- "))
# stop=int(input("Enter the last number:- "))
# for evodd in range(start,stop):
#     if evodd%2==0:
#         print("The number is even:- ",evodd)
#     elif evodd%2!=0:
#         print("The number is odd:-",evodd)

# year=int(input("Enter the year:- "))
# if year%4==0 and year%100!=0 and year%400!=0:
#  print("This is a leap year:- ",year )
# else:
#  print("This is not a leap year:- ",year)

start_year=int(input("Enter the start year: "))
end_year=int(input("Enter the end year: "))

leap_year=[]
for year in range(start_year, end_year+1):
    
    leap_years.append(year)

if len(leap_year)>0: