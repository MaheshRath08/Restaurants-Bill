print("Thanks for coming in...")
print("Hopefully You had an amazing experience...")
subTotal = float(input("Sub-Total Amount:\n"))
tip = float(input("Tips respect to the sub-total Amount (in %):\n"))
gst = 0.05
totalAmount = subTotal + (subTotal * gst) + (subTotal * (tip/100))
print("Your Total payable amount is Rs. "+ str(totalAmount)) 