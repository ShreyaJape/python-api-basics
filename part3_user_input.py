"""
Part 3: Dynamic Queries with User Input
=======================================
Difficulty: Intermediate

Learn:
- Using input() to make dynamic API requests
- Building URLs with f-strings
- Query parameters in URLs
"""

import requests


def get_user_info():
    """Fetch user info based on user input."""
    print("=== User Information Lookup ===\n")

    user_id = input("Enter user ID (1-10): ")

    if not user_id.isdigit():
        print("invalid user id, please enter valid user id")
        

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n--- User #{user_id} Info ---")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Website: {data['website']}")
    else:
        print(f"\nUser with ID {user_id} not found!")


def search_posts():
    """Search posts by user ID."""
    print("\n=== Post Search ===\n")

    user_id = input("Enter user ID to see their posts (1-10): ")

    if not user_id.isdigit():
        print("please enter valid user id in digits")
    user_id = int(user_id)   
    # Using query parameters
    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}

    response = requests.get(url, params=params)
    posts = response.json()

    if posts:
        print(f"\n--- Posts by User #{user_id} ---")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post['title']}")
    else:
        print("No posts found for this user.")


def get_crypto_price():
    """Fetch cryptocurrency price based on user input."""
    print("\n=== Cryptocurrency Price Checker ===\n")

    print("Available coins: btc-bitcoin, eth-ethereum, doge-dogecoin")
    coin_id = input("Enter coin ID (e.g., btc-bitcoin): ").lower().strip()

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price_usd = data['quotes']['USD']['price']
        change_24h = data['quotes']['USD']['percent_change_24h']

        print(f"\n--- {data['name']} ({data['symbol']}) ---")
        print(f"Price: ${price_usd:,.2f}")
        print(f"24h Change: {change_24h:+.2f}%")
    else:
        print(f"\nCoin '{coin_id}' not found!")
        print("Try: btc-bitcoin, eth-ethereum, doge-dogecoin")


# Exercise 1 
def get_city_coordinates(city):
    """
    Convert city name to latitude and longitude
    using Open-Meteo Geocoding API.
    """
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city,
        "count": 1
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None, None

    data = response.json()

    if "results" not in data:
        return None, None

    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]

    return latitude, longitude

def get_weather():
    """Fetch current weather for a city."""
    print("\n=== Weather Checker ===\n")

    city = input("Enter city name: ").strip()

    latitude, longitude = get_city_coordinates(city)

    if latitude is None:
        print("City not found!")
        return

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        weather = response.json()["current_weather"]

        print(f"\n--- Weather in {city.title()} ---")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Wind Speed: {weather['windspeed']} km/h")
        print(f"Weather Code: {weather['weathercode']}")
    else:
        print("Failed to fetch weather data.")

# Excercise 2
    print("----Todo search----------")
def todo_search():
    status = input("Enter the value (true/false) :").lower()
    url = "https://jsonplaceholder.typicode.com/todos"
    # Query parameter
    params = {"completed": status}

    response = requests.get(url,params=params)
    todos = response.json()

# Print result
    print(f"\nNumber of todos with completed = {status}: {len(todos)}\n")

# Print first 5 todos
    for i, todo in enumerate(todos[:5], 1):
        print(f"{i}. {todo['title']}")








def main():
    """Main menu for the program."""
    print("=" * 40)
    print("  Dynamic API Query Demo")
    print("=" * 40)

    while True:
        print("\nChoose an option:")
        print("1. Look up user info")
        print("2. Search posts by user")
        print("3. Check crypto price")
        print("4. weather info")
        print("5. todo search")
        print("6. Exit")
        

        choice = input("\nEnter choice (1-6): ")

        if choice == "1":
            get_user_info()
        elif choice == "2":
            search_posts()
        elif choice == "3":
            get_crypto_price()
        elif choice == "4":
            get_weather()
        elif choice == "5":
            todo_search()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# --- EXERCISES ---
#
# Exercise 1: Add a function to fetch weather for a city
#             Use Open-Meteo API (no key required):
#             https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true
#             Challenge: Let user input city name (you'll need to find lat/long)
#
# Exercise 2: Add a function to search todos by completion status
#             URL: https://jsonplaceholder.typicode.com/todos
#             Params: completed=true or completed=false
#
# Exercise 3: Add input validation (check if user_id is a number)
