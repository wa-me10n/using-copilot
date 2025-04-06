import requests

def get_random_joke():
    """
    Fetches a random joke from the Official Joke API.
    Returns the joke as a string.
    """
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    except requests.exceptions.RequestException as e:
        return f"Error fetching joke: {e}"

if __name__ == "__main__":
    print("Here's a random joke for you:")
    print(get_random_joke())