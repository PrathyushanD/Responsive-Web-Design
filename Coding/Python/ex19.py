def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use varibles from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math indise too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, varibles and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #This shows all the different ways we'reable to give our function cheese_and_crackers the values it needs to print them. We can give it staright numbers. We can give it varibles. We can give it math. We can even ccombine math and varibles.
