#PAYMENT-MANAGER
#Python Exercise 44: Design a program that calculates the amount to be paid for a product
#Considering its normal price and payment terms:
#Cash/pix: 10% discount
#Cash on the card: 5% discount
#Up to 2x on the card: formal price
#3x or more on the card: 20% fees
print('{:=^40}'.format(' \033[032mVERISSIMO IMPORTS\033[m '))
price = float(input("Price of product:U$"))
paytype = int(input("For payment type digit: \033[036m\n[1] Cash/PIX\n[2] Debit\n[3] "
                    "Credit Card 2x\n[4] Credit Card 3x or more\033[m\nDigit the payment type: "))

if paytype == 1:
    total = price - (price * 0.1)
elif paytype == 2:
    total = price - (price * 0.05)
elif paytype == 3:
    installment = price / 2
    print("And will stay in 2x installments of {:.2f}U$.".format(installment))
elif paytype == 4:
    total = price + (price * 0.2 )
    totalinstall = int(input("How many installments? "))
    installments = total / totalinstall
    print("Your buy with {}x installments, and with fees will be \033[033m{:.2f}U$\033[m .".format(totalinstall,installments))
print("Your product worth \033[032m{:.2f}U$\033[m, and will stay \033[032m{:.2f}U$\033[m".format(price,total))