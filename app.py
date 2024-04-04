# from flask import Flask, render_template, request
# from accessing_custom_scenario import access_custom_scenario, bot_endpoint, scenario_name

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         user_message = request.form.get("user_message")
#         # Call your Python function to access the custom scenario
#         response = access_custom_scenario(bot_endpoint, scenario_name, user_message)
#         # Process the response (optional)
#         if response:
#             bot_response = response
#         else:
#             bot_response = "Error: Could not access Health Bot scenario."
#         return render_template("response.html", bot_response=bot_response)
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)














import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Define the Health Bot endpoint and scenario name
bot_endpoint = "https://covid19_core.azurewebsites.net/v1/dialogs"
scenario_name = "covid19_core"
jwt_token = os.getenv("JWT_TOKEN")

def access_custom_scenario(bot_endpoint, scenario_name, user_message=None):
    """
    Sends a request to the Health Bot API to trigger the custom scenario.

    Args:
        bot_endpoint (str): The URL endpoint of your Health Bot.
        scenario_name (str): The name of the custom scenario to trigger.
        user_message (str, optional): An optional user message to send to the bot.

    Returns:
        dict: The response from the Health Bot API, or None on error.
    """

    headers = {
        "Authorization": f"Bearer {jwt_token}"
    }
    data = {
        "scenarioName": scenario_name
    }
    if user_message:
        data["userQuery"] = user_message

    url = f"{bot_endpoint}"

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error accessing Health Bot scenario: {e}")
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_message = request.form.get("user_message")
        # Call your Python function to access the custom scenario
        response = access_custom_scenario(bot_endpoint, scenario_name, user_message)
        # Process the response (optional)
        if response:
            bot_response = response
        else:
            bot_response = "Error: Could not access Health Bot scenario."
        return render_template("response.html", bot_response=bot_response)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=8086)

