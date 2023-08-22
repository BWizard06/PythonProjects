import requests
from termcolor import colored


request_url = "http://www.boredapi.com/api/activity/"
response = requests.get(request_url)
answer = input(colored("If you are bored you can generate a random activity, do you want to generate one?(y, n) ", "green"))

if response.status_code == 200:
    data = response.json()
    activity = data["activity"]
    type = data["type"]
    participants = data["participants"]
    price = data["price"]
    if answer[0].capitalize() == "Y":
        print(colored(f"""\n
Activity:     {activity}
Type:         {type}
Participants: {participants}
Price:        {price}""", "cyan"))
    else:
        print("Alright come back when you are bored again")


