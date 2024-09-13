#Bill Nguyen | Lab 2: Birthday Paradox | 9/12
import random

def birthdays(numOfPeople):
    return [random.randint(1,365) for n in range(numOfPeople)]

def dups(birthdays):
    return len(birthdays) != len(set(birthdays))

def birthdayLists(numberOfPeople, runs = 1000):
    duplicates = 0
    for i in range(runs):
        birthDays = birthdays(numberOfPeople)
        if dups(birthDays):
            duplicates += 1


    return (duplicates/runs) * 100


def experiment():
    print(f"Birthday Paradox Simulation Results: \nn | Probability(%)")

    results = []
    for x in range(5,55,5):
        probability = birthdayLists(x)
        result = f"{x} | {probability:.2f}%"
        results.append(result)
        print(results)

    with open("lab2/analysis/results.txt", "w") as resultFile:
        resultFile.write(f"Birthday Paradox Simulation Results: \nn | Probability(%)\n")
        resultFile.write(f"\n".join(results))
    
def main():
    while True:
        try:
            experiment()
            repeat = input("Would you like to try this again?(Y|N)").upper() #WILL AUTOMATICALLY MAKE EVERY REPLY TO THIS CAPITALIZE
            if repeat != 'Y':   
                break
        except ValueError: #Will print an ValueError for an exception
            print("ValueError")
        except ZeroDivisionError:  #Will print an ZeroDivisionError for an exception
            print("ZeroDivisionError")     
        
main()