# import requests
# from azure.identity import DefaultAzureCredential

# def get_scenario_names(health_bot_name, resource_group):
#     """Retrieves scenario names from Azure Health Bot using Azure Management API."""
#     credential = DefaultAzureCredential()
#     token = credential.get_token("https://management.azure.com/")

#     headers = {
#         "Authorization": f"Bearer {token.token}",
#         "Content-Type": "application/json"
#     }

#     url = f"https://management.azure.com/subscriptions/078d8b6e-a76a-4127-a484-4f05c5b95caa/resourceGroups/{resource_group}/providers/Microsoft.HealthBot/botServices/{health_bot_name}/scenarios?api-version=2021-09-01-preview"
    
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         scenario_names = [scenario["name"] for scenario in response.json().get("value", [])]
#         return scenario_names
#     else:
#         print(f"Error retrieving scenario names: {response.status_code} - {response.text}")
#         return None

# if __name__ == "__main__":
#     health_bot_name = "healthbot-poc-1"
#     resource_group = "POC_HealthBot"
#     scenario_names = get_scenario_names(health_bot_name, resource_group)

#     if scenario_names:
#         print("Scenario names:")
#         for name in scenario_names:
#             print(name)








# import requests

# def get_scenario_names(jwt_token, health_bot_name, resource_group):
#     """Retrieves scenario names from Azure Health Bot using Azure Management API."""
#     headers = {
#         "Authorization": f"Bearer {jwt_token}",
#         "Content-Type": "application/json"
#     }

#     url = f"https://management.azure.com/subscriptions/078d8b6e-a76a-4127-a484-4f05c5b95caa/resourceGroups/{resource_group}/providers/Microsoft.HealthBot/botServices/{health_bot_name}/scenarios?api-version=2021-09-01-preview"
    
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         scenario_names = [scenario["name"] for scenario in response.json().get("value", [])]
#         return scenario_names
#     else:
#         print(f"Error retrieving scenario names: {response.status_code} - {response.text}")
#         return None

# if __name__ == "__main__":
#     jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnROYW1lIjoibXlUZW5hbnQiLCJpYXQiOiIxNTA3MDU2OTAwIn0.MN4DcxO2mLsltEYNpXbC6T6Bjxj3-rxIAObngZIw4-U"
#     health_bot_name = "healthbot-poc-1"
#     resource_group = "POC_HealthBot"
#     scenario_names = get_scenario_names(jwt_token, health_bot_name, resource_group)

#     if scenario_names:
#         print("Scenario names:")
#         for name in scenario_names:
#             print(name)





# import requests

# def get_scenario(jwt_token, health_bot_name, resource_group, scenario_id):
#     """Retrieves a specific scenario from Azure Health Bot using Azure Management API."""
#     headers = {
#         "Authorization": f"Bearer {jwt_token}",
#         "Content-Type": "application/json"
#     }

#     url = f"https://centralindia.healthbot.microsoft.com/account/healthbot-poc-1-eosj397"
    
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         scenario = response.json()
#         return scenario
#     else:
#         print(f"Error retrieving scenario: {response.status_code} - {response.text}")
#         return None

# if __name__ == "__main__":
#     jwt_token = "f4eea334e4ffa08994f828f45f42492da886767e131023bfd9f64f5fa239c35a"
#     health_bot_name = "healthbot-poc-1"
#     resource_group = "POC_HealthBot"
#     scenario_id = "Extend_triage_with_handoff"
    
#     scenario = get_scenario(jwt_token, health_bot_name, resource_group, scenario_id)

#     if scenario:
#         print("Scenario details:")
#         print(scenario)









# import requests

# def get_scenario(jwt_token, health_bot_name, resource_group):
#     """Retrieves a specific scenario from Azure Health Bot using Azure Management API."""
#     headers = {
#         "Authorization": f"Bearer {jwt_token}",
#         "Content-Type": "application/json"
#     }

#     url = f"https://centralindia.healthbot.microsoft.com/api/account/healthbot-poc-1-eosj397/scenarios"
    
#     response = requests.get(url, headers=headers)
    
#     if response.status_code == 200:
#         try:
#             scenario = response.json()
#             return scenario
#         except ValueError as e:
#             print(f"Error parsing JSON: {e}")
#             return None
#     else:
#         print(f"Error retrieving scenario: {response.status_code} - {response.text}")
#         return None

# if __name__ == "__main__":
#     jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnROYW1lIjoiaGVhbHRoYm90LXBvYy0xLWVvc2ozOTciLCJpYXQiOjE3MTEwMTM1NDV9.LeBcEr9XELw7ZVe9PLScZ0KBYfR8UpAdYcLD7w_EW3U"
#     health_bot_name = "healthbot-poc-1"
#     resource_group = "POC_HealthBot"
#     # scenario_id = "Extend_triage_with_handoff"
    
#     scenario = get_scenario(jwt_token, health_bot_name, resource_group)

#     if scenario:
#         print("Scenario details:")
#         print(scenario)







# import requests

# # Direct Line API endpoint for retrieving a single activity
# api_url = "https://directline.botframework.com/v3/directline/conversations/AyWrNUcfk2y51X0JkGvxOE-in/activities/AyWrNUcfk2y51X0JkGvxOE-in|0000004"

# # Replace <DIRECT_LINE_SECRET> with your actual Direct Line secret
# headers = {
#     "Authorization": "Bearer yJVXqnABSz4.LNaXnp-jow1eWB5p5xYQdhpVdn72A1FetoIDq90cj78"
# }

# # Send a GET request to retrieve the activity details
# response = requests.get(api_url, headers=headers)

# # Print the activity details
# print(response.json())







import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

def generate_direct_line_token():
    direct_line_secret = os.getenv("DIRECT_LINE_SECRET")
    if not direct_line_secret:
        raise ValueError("Direct Line secret not found in environment variables")

    token_endpoint = "https://directline.botframework.com/v3/directline/tokens/generate"

    response = requests.post(token_endpoint, headers={"Authorization": f"Bearer {direct_line_secret}"})
    if response.status_code == 200:
        return response.json().get("token")
    else:
        raise ValueError(f"Failed to generate Direct Line token: {response.text}")

@app.route("/")
def home():
    try:
        direct_line_token = generate_direct_line_token()
        return render_template("example.html", direct_line_token=direct_line_token)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True, port=7282)








