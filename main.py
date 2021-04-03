from api import getSigns, getHoroscope
##pip install requests

signs = getSigns()
timeframe = input("Do you want your horoscope for 'today', 'tomorrow', or 'yesterday'")
print("hey please select your sign:")


for sign in signs:

    print(f'  - {sign}')##fetching the signs from the api

selectedSign = input(" select your sign:\n") ##using /n to get user input

horoscopeDict = getHoroscope(selectedSign, timeframe)

print("\n")
print(horoscopeDict["horoscope"])
print('Authour souvik dutta')

