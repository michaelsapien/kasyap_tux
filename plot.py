import requests
import matplotlib.pyplot as plt
from datetime import datetime

def fetch_wind_gust_data(latitude, longitude):
    # Define the API endpoint and parameters
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=windgusts_10m&timezone=Asia/Kolkata"

    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful kasyap 
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to retrieve the data. Status code:", response.status_code)
        return None

def plot_wind_gusts(data):
    # Check if the required data exists in the response
    if 'hourly' in data and 'windgusts_10m' in data['hourly'] and 'time' in data['hourly']:
        wind_gusts = data['hourly']['windgusts_10m']
        print(wind_gusts)
        timestamps = data['hourly']['time']

        # Convert timestamps to datetime objects
        times = [datetime.fromisoformat(ts) for ts in timestamps]

        # Plot the wind gusts
        plt.figure(figsize=(10, 5))
        plt.plot(times, wind_gusts, label='Wind Gusts (m/s)', color='blue')
        plt.xlabel('Time')
        plt.ylabel('Wind Gusts (m/s)')
        plt.title('Hourly Wind Gusts in Bengaluru')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.legend()
        plt.show()
    else:
        print("Wind Gusts data not found in the response.")

def main():
    print('test data')
    latitude = 12.9716
    longitude = 77.5946

    # Fetch wind gust data
    data = fetch_wind_gust_data(latitude, longitude)

    # Plot wind gust data if available
    if data:
        plot_wind_gusts(data)

if __name__ == "__main__":
    main()
