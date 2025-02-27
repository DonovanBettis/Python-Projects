import random


def generateTicket():
    lottery_ticket = []
    for i in range(0, 6):
        num = random.randint(0, 9)
        lottery_ticket.append(num)
    return lottery_ticket


def generateBiasedTicket():
    biased_ticket = []
    for i in range(0, 2):
        num1 = random.randint(0, 3)
        biased_ticket.append(num1)
    for i in range(0, 2):
        num2 = random.randint(4, 6)
        biased_ticket.append(num2)
    for i in range(0, 2):
        num3 = random.randint(0, 9)
        biased_ticket.append(num3)
    return biased_ticket


def getUserTicket():
    user_ticket = []
    for i in range(0, 6):
        num = int(input("Please enter a single digit number between 0 and 9: "))
        if num > 9:
            print("Please enter a single digit number")
            num = int(input("Please enter a single digit number between 0 and 9: "))
        user_ticket.append(num)
    return user_ticket


def CompareTickets(UserTicket, LotteryTicket):
    MatchesList = [x for x in UserTicket if x in LotteryTicket]
    Matches = len(MatchesList)
    return Matches


choice = input("Do you want to generate lottery tickets? Enter Y or N: ").upper()
while choice == 'Y':

    LotteryTicket = generateTicket()
    BiasedTicket = generateBiasedTicket()
    UserTicket = getUserTicket()

    print("Lottery Ticket: " + str(LotteryTicket))
    print("User Ticket: " + str(UserTicket))

    MatchingNumbers = CompareTickets(UserTicket, LotteryTicket)
    print("# of matched digits = " + str(MatchingNumbers))
    TotalNumbers = 6
    print("# of unmatched digits = " + str(TotalNumbers - MatchingNumbers))

    print("\n\nBiased Ticket: " + str(BiasedTicket))
    print("User Ticket: " + str(UserTicket))
    BiasedMatched = CompareTickets(UserTicket, BiasedTicket)
    print("# of matched digits = " + str(BiasedMatched))
    print("# of unmatched digits = " + str(TotalNumbers - BiasedMatched))

    choice = input("Do you want to generate lottery tickets? Enter Y or N: ").upper()
