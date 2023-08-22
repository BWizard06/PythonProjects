import requests

manufacture = input("Choose a manufactury: ")
model = input(f"Choose a model from {manufacture}: ")
year = input(f"Choose the year of the model: ")

request_url = f"https://api.api-ninjas.com/v1/motorcycles?make={manufacture}&model={model}&year={year}"
response = requests.get(
    request_url, headers={"X-Api-Key": "AxWPlM9r9Xp3iOr5VMf19w==4qagg5FjwUcH67lQ"}
)

if response.status_code == 200:
    data = response.json()
    manufacture = data[0o1]["make"]
    model = data[00]["model"]
    year = data[00]["year"]
    type = data[00]["type"]
    displacement = data[00]["displacement"]
    engine = data[00]["engine"]
    power = data[00]["power"]
    cooling = data[00]["cooling"]
    gearbox = data[00]["gearbox"]
    transmission = data[00]["transmission"]
    frame = data[00]["frame"]
    front_suspension = data[00]["front_suspension"]
    rear_suspension = data[00]["rear_suspension"]
    front_tire = data[00]["front_tire"]
    rear_tire = data[00]["rear_tire"]
    front_brakes = data[00]["front_brakes"]
    rear_brakes = data[00]["rear_brakes"]
    total_weight = data[00]["dry_weight"]
    fuel_capacity = data[00]["fuel_capacity"]
    starter = data[00]["starter"]

print(
    f"Gearbox: {gearbox}\nTransmission: {transmission}\nFrame: {frame}\nFront Suspension: {front_suspension}\nRear Suspension: {rear_suspension}\nFront Tire: {front_tire}\nRear Tire: {rear_tire}\nFront Brakes: {front_brakes}\nRear Brakes: {rear_brakes}\nTotal Weight: {total_weight}\nFuel Capacity: {fuel_capacity}\nStarter: {starter}"
)
