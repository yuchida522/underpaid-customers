

def accounting(path):

    melon_cost = 1.00
    order_log = open(path)

    #iterate over each 
    for line in order_log:
        line = line.rstrip()
        #split line where "|" is to get the info
        info = line.split("|")

        #get info and save it to variables

        #customer name
        customer = info[1]
        
        #how many melons they bought and how much they paid
        melons_bought = float(info[2])
        amount_paid = float(info[3])
    
        #calculate how much the sale should have costed
        correct_sale = melon_cost * melons_bought
        
        #checks if the sale in the report is correct, and if not print how much they paid and how much was expected

        if correct_sale != amount_paid:
            print(f"{customer} paid {amount_paid:.2f}, expected {correct_sale:.2f}.")

        #if correct_sale < 


    order_log.close()
    
accounting("customer-orders.txt")
    
    

