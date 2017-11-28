#Python3,mvs, 2017-09-27
#Chapter 5 / Assignment 6 / Loan calculation
import math
import datetime
now = datetime.datetime.now()
current_year=now.year

def show_balance(remaining,interest,payment,year):
    interest_pay=remaining*interest #Zinsen
    repayment=payment-interest_pay #Tilgung
    next_remaining=remaining-repayment #Verbleibender Kredit
    next_year=year+1 #Nächstes Jahr
    print("%i: Zinsen: %8.2f EUR, Tilgung: %8.2f EUR, Restschuld: %8.2f EUR" % (year,interest_pay,repayment,next_remaining))
    if(next_remaining<(payment-next_remaining*interest)): #ENDE wenn Kredit im nächsten Jahr bedient wird
        print("Kredit endet im Jahr %i mit Restbetrag %8.2f EUR." % (next_year,next_remaining))
    else :
        show_balance(next_remaining,interest,payment,next_year)
    return

mortgage_in=float(input("Wieviel Geld möchten Sie aufnehmen [EUR]?: "))
interest_in=float(input("Wie hoch ist Ihr stabiler Zinssatz [%]?: "))/100.0
return_in=float(input("Wieviel Geld möchten Sie pro Monat inklusive Zinsen zurückzahlen [EUR]?: "))

print("Rückzahlungsplan:")

return_year=return_in*12.0
if(interest_in*mortgage_in>=return_year):
    print("Ihre Tilgungsrate ist leider zu niedrig.")
elif(return_year-interest_in*mortgage_in>mortgage_in) :
    print("Ihre Tilgungsrate ist leider zu hoch.")
else :
    show_balance(mortgage_in,interest_in,return_year,current_year)

print("Ende des Programms") 
