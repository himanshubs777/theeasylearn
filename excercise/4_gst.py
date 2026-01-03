# write a program to calculate  GST tax amount frome given bill amount annd tax rate

bill_amount = 0
gst_rate = 0

bill_amount = input("Enter the bill amount :")
gst_rate = input("Enter the GST rate :")
bill_amount=float(bill_amount)
gst_rate=float(gst_rate)

GST = (bill_amount * gst_rate) / 100

print("GST amount is :", GST)