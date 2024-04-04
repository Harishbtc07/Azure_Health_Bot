# import requests

# def access_custom_scenario(bot_endpoint, scenario_name, user_message=None):
#     """
#     Sends a request to the Health Bot API to trigger the custom scenario.

#     Args:
#         bot_endpoint (str): The URL endpoint of your Health Bot.
#         scenario_name (str): The name of the custom scenario to trigger.
#         user_message (str, optional): An optional user message to send to the bot.

#     Returns:
#         dict: The response from the Health Bot API, or None on error.
#     """

#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnROYW1lIjoiaGVhbHRoYm90LXBvYy0xLWVvc2ozOTciLCJpYXQiOjE3MTE5NTAxNjF9.Ffpc8tZ_BmsgNao6YO1whaBaAZOjNscxsyLAWasRhjE"  # Replace with your bot's access token
#     }
#     data = {
#         "scenarioName": scenario_name
#     }
#     if user_message:
#         data["userQuery"] = user_message

#     url = f"{bot_endpoint}/v1/dialogs"

#     try:
#         response = requests.post(url, headers=headers, json=data)
#         response.raise_for_status()  # Raise an exception for non-200 status codes
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"Error accessing Health Bot scenario: {e}")
#         return None

# # Replace with your Health Bot endpoint and scenario name
# bot_endpoint = "nslookup symptom_tracker.azurewebsites.net"
# scenario_name = "symptom_tracker"

# # Optional: Include a user message to send with the scenario trigger
# user_message = "Start custom scenario"

# response = access_custom_scenario(bot_endpoint, scenario_name, user_message)

# if response:
#     print("Response from Health Bot:")
#     print(response)
# else:
#     print("Error accessing Health Bot scenario.")