# Trust Fund Buddy - Bad
# Demonstrates a logical error

print(
"""
		TRUST FUND BUD

Totals you monthly spending so that your trust fund doesn't run out
(an you're forced do get a real job).
lease enter the requested, monthly costs. Since you're rich, ignore pennies and use only dollar amounts.

"""
)
car = int(input ("Lamborghini Tune-Ups: "))
rent = int(input("Manhattan Apartment: "))
jet = int(input("Private Jet Rental: "))
gifts = int(input("Gifts: "))
food = int(input ("Dining Out: "))
staff = int(input("Staff (butlers, chef, driver, assistant): "))
guru = int(input("Personal Guru and Coach: "))
games = int(input ("Computers Games: "))

total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total:", total)
input("\n\nPress the enter key to exit.")
