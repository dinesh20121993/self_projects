import requests
url_api = "https://randomuser.me/api"
def generate_usr():
    response = requests.request(method = "get",url = url_api).json()
    user_data = {}
    name = response["results"][0]["name"]
    full_name = name['title'] +" " + name["first"] +" " + name["last"]
    user_data["name"] = full_name
    user_data["gender"] = response["results"][0]["gender"]
    address = f'{response["results"][0]["location"]["city"]}, {response["results"][0]["location"]["state"]}, {response["results"][0]["location"]["country"]}, {response["results"][0]["location"]["postcode"]}'
    user_data["address"] = address
    user_data["e-mail"] = response["results"][0]["email"]
    user_data["user_name"] = response["results"][0]["login"]["username"]
    user_data["password"] = response["results"][0]["login"]["password"]
    user_data["age"] = response["results"][0]["dob"]["age"]
    return user_data