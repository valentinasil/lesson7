print('-'*65)
print('100th Birthday Program: ')
print()

print('Description: This program ask for your current age and tells you the year that you will turn 100 ')
print()

age = input('what is your age today? ')
age =int(age)

year = (100 - age) + 2018 
year=str(year)
year=('you will turn 100 in the year ' +year)
print(year)
print('-'* 65)
print()