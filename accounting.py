

def accounting(path):

    melon_cost = 1.00
    order_log = open(path)

    #split the report to parts
    for line in order_log:
        line = line.rstrip()
        info = line.split("|")

        #create variables to work with
        customer = info[1]
        melons_bought = info[2]
        amount_paid = info[3]
    
        #see how much the sale should have costed
        correct_sale = melon_cost * int(melons_bought)
        
        #checks if the sale is correct, and if the sale does not match the actual cost:
        #print statment

        if float(correct_sale) != float(amount_paid):
            print(f"{customer} paid {float(amount_paid):.2f}, expected {float(correct_sale):.2f}.")


    order_log.close()
    
accounting("customer-orders.txt")
    
    

