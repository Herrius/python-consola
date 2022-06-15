import os
import art
#HINT: You can call clear() to clear the output in the console.
audiction=[]
def bid_max(audiction_list):
    max_bid=int()
    winner=""
    for index in audiction_list:
        if index['bid'] > max_bid:
            max_bid=index['bid']
            winner=index['name']
    print(f"the winner of bid is {winner} with amount ${max_bid}")

def main():
    process_end=False
    while not process_end:
        print(art.logo)
        name=input("Writing its name: ")
        bid=int(input("Writing its bid price: $"))
        client={}
        client["name"]=name
        client["bid"]=bid
        audiction.append(client)
        answer=input("would do you write other bid?")
        if answer=='no':
            process_end=True
        else:
            os.system('cls')
    bid_max(audiction)
    
main()
