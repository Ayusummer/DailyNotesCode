from azure.identity import DeviceCodeCredential
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import httpx
import configparser


# Function to read credentials from config file
def read_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config["azure"]


# Authenticate with Device Code Credential
def authenticate(config):
    credential = DeviceCodeCredential(
        client_id=config["clientId"], tenant_id=config["tenantId"]
    )
    return credential


# Function to get events
def get_events(credential, start_date, end_date):
    token = credential.get_token("https://graph.microsoft.com/.default").token
    headers = {"Authorization": f"Bearer {token}"}
    events_url = f"https://graph.microsoft.com/v1.0/me/calendarview?startdatetime={start_date}&enddatetime={end_date}"
    response = httpx.get(events_url, headers=headers)
    return response.json().get("value", [])


# Plotting function
def plot_events(events):
    # Categorize and count events
    categories = {}
    for event in events:
        category = event.get("categories", ["Uncategorized"])[0]
        categories[category] = categories.get(category, 0) + 1

    # Plotting the pie chart
    plt.figure(figsize=(10, 6))
    plt.pie(categories.values(), labels=categories.keys(), autopct="%1.1f%%")
    plt.title("Event Categories in the Last Week")
    plt.show()


# Main function
def main():
    config = read_config("config.cfg")
    credential = authenticate(config)
    print(
        f"Access token: {credential.get_token('https://graph.microsoft.com/.default').token}"
    )

    # Define the time range for the past week (last Monday to Friday)
    today = datetime.today()
    last_monday = today - timedelta(days=today.weekday() + 7)
    last_friday = last_monday + timedelta(days=4)

    start_date = last_monday.strftime("%Y-%m-%dT00:00:00")
    end_date = last_friday.strftime("%Y-%m-%dT23:59:59")

    events = get_events(credential, start_date, end_date)
    print(f"Events: {events}")
    plot_events(events)


if __name__ == "__main__":
    main()
