def convert_sar_to_inr(sar_amount):
    inr_total=sar_amount *22.5
    return inr_total
    
my_monthly_savings = 30000

savings_in_rupees = convert_sar_to_inr(my_monthly_savings)

print("Total money transfer to parents:₹"+ str(savings_in_rupees) + "INR")



