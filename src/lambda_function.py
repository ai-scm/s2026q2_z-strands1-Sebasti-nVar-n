from strands import Agent, tool
from strands_tools import http_request
from typing import Dict, Any
import boto3
import os
import json

ddb = boto3.resource('dynamodb')
table = ddb.Table(os.environ['SESSIONS_TABLE'])

def get_session_history(session_id: str) -> list:
    """Retrieve conversation history for a session."""
    try:
        response = table.get_item(Key={'sessionID': session_id})
        if 'Item' in response:
            return json.loads(response['Item']['messages'])
        return []
    except Exception as e:
        print(f"Error retrieving session history: {e}")
        return []

def update_session_history(session_id: str, messages: list):
    """Update conversation history for a session."""
    try:
        table.put_item(
            Item={
                'sessionID': session_id,
                'messages': json.dumps(messages)
            }
        )
    except Exception as e:
        print(f"Error updating session history: {e}")

# Define a travel-focused system prompt
TRAVEL_AGENT_PROMPT = """You are a travel assistant that can help customers book their travel.

If a customer wants to book their travel, assist them with flight options for their destination and provide them with information about the weather.

Use the flight_search tool to provide flight carrier choices for their  destination.

You can provide information about the weather with the following:
1. Make HTTP requests to the National Weather Service API
2. Process and display weather forecast data
3. Provide weather information for locations in the United States
4. The Seattle zip code value is 98101 and the latitude and longitude   coordinates are 47.6061° N, 122.3328° W
5. First get the coordinates or grid information using https://api.weather. gov/points/{latitude},{longitude} or https://api.weather.gov/points/{zipcode}
6. Then use the returned forecast URL to get the actual forecast

When displaying responses:
- Format weather data in a human-readable way
- Highlight important information like temperature, precipitation, and alerts
- Handle errors appropriately
- Convert technical terms to user-friendly language

Always explain the weather conditions clearly and provide context for the forecast.

Provide the users with a friendly customer support response that includes available flights and the weather for their destination.

"""

@tool
def flight_search(city: str) -> dict:
    """Get available flight options to a city.

    Args:
        city: The name of the city
    """
    flights = {
        "Atlanta": [
            "AnyCompany01 Airlines",
            "AnyCompany09 Airlines"
        ],
        "Seattle": [
            "AnyCompany05 Airlines",
            "AnyCompany02 Airlines"
        ],
        "New York": [
            "AnyCompany03 Airlines",
            "AnyCompany08 Airlines"
        ]
    }
    return flights[city]

def handler(event: Dict[str, Any], _context) -> str:
    # Get session history
    session_history = get_session_history(event["user"]["session_id"])
    travel_agent = Agent(
        model="us.amazon.nova-lite-v1:0",
        system_prompt=TRAVEL_AGENT_PROMPT,
        tools=[flight_search, http_request],
        messages=session_history
    )

    response = travel_agent(event.get('prompt'))

    # Update session history
    update_session_history(event["user"]["session_id"], travel_agent.   messages)
    return str(response)
