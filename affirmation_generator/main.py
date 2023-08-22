import requests
from termcolor import colored

request_url = "https://www.affirmations.dev/"
response = requests.get(request_url)
answer = input(colored("Do you want to generate a quote?(y, n) ", "green"))


    
while True:
    request_url = "https://www.affirmations.dev/"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        affirmation = data["affirmation"]
        if answer[0].capitalize() == "Y":
            print("Your quote is: ")
            print(colored(affirmation, "blue"))
            print("\n")
            answer = input(colored("Do you want to generate another quote? ", "green"))
        else:
            print(colored("\nCome back when you want to generate a quote :)", "red"))
            break
