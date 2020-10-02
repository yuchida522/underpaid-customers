

def accounting(path):

    melon_cost = 1.00
    order_log = open(path)

    #split the report to parts
    for line in order_log:
        line = line.rstrip()
        info = line.split("|")
        print(info)

    order_log.close()
    
accounting("customer-orders.txt")
    #create variables to work with
    #see how much the sale should have costed
    #see how much the customer paid
    #if the sale does not match the actual cost:
        #print statment

