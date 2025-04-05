"""
#GAS-PRICE-CONVERTION (header)
this is an executable file that aims to convert gas type to its price
My
"""
def gasPriceConvertion(gas_type):
    #in case of invalid input
    #make sure the program does not require user input to be case sensitive, make sure user's input will still be accepted if they put spaces in between their input.
    if (gas_type != "R" and gas_type != "r" and gas_type != "MG" and gas_type != "mg" and gas_type != "Mg" and gas_type !="M g" and gas_type !="M G" and gas_type !="m g"and gas_type != "P" and gas_type != "p"):
        return str("not calculable, you have entered an invalid input, please enter letter 'r' for regular gas, 'mg' for mid-grade gas, or letter 'p' for premium gas \n") ;
        #convert gas type to

    elif (gas_type == "R" or gas_type == "r"):
        regular_price = 3.741; # assign a value to the local variable regular_price
        #second user input
        # a boolean to ensure input is a number
        input_price = input("How much regular gas are you pumping? Enter a number:\n")
        if input_price.isdigit():
            input_price = float(input_price)  # Convert the input to float
            total_price = regular_price * input_price
            return str(total_price)  # Convert total_price to string for returning
        else:
            return "Not calculable, please enter a number and try again."

    elif (gas_type == "mg" or gas_type == "MG" or gas_type =="Mg" or gas_type =="M g" or gas_type =="M G" or gas_type =="m g"):
        midgrade_price = 4.103;# assign a value to the local variable midgrade_price
        #second user input
        input_price = input("how much mid-grade gas are you pumping? enter a number  \n");
        if input_price.isdigit() == True:
            input_price = float(input_price);
            total_price = midgrade_price * input_price;
            return str(total_price);
        else: return ("not calculable, please enter a number and try again");

    elif (gas_type == "p" or gas_type =="P"):
        premium_price = 4.221; # assign a value to the local variable premium_price
        #second user input
        input_price = input("how much premium gas are you pumping? enter a number  \n");
        if input_price.isdigit() == True:
            input_price = float(input_price);
            total_price = premium_price * input_price;
            return str(total_price);
        else: return ("not calculable, please enter a number and try again");


gas_type = input("What kind of gas are you pumping ?\nHint: enter letter 'r' for regular gas, letters 'mg' for mid-grade gas , or letter 'p' for premium gas \n");
#final price in complete sentence'
print("the price of your gas is " + gasPriceConvertion(gas_type));