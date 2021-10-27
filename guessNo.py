import random


class NumberGuessing:

    def __init__(self):
      self.LOWER = 1
        self.HIGHER = 75

    def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)

 
    def start(self):
      
        random_number = self.get_random_number()

        print(
            f"what is the guessed number from {self.LOWER} to {self.HIGHER}")

     
        chances = 0
        while True:
            user_number = int(input("Enter guessed number: "))
            if user_number == random_number:
                print(
                    f"->  it is coreect in {chances + 1} step{'s' if chances > 1 else ''}!")
                break
            elif user_number < random_number:
                print("-> entered number is lower than the guessed")
            else:
                print("->  entered number is higher than the guessed")
            chances += 1


numberGuessingGame = NumberGuessingGame()
numberGuessingGame.start()
