import requests
import json

def dogbreedname():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch: {response.status_code}")
        return None

    try:
        data = response.json()
    except Exception as e:
        print("JSON error:", e)
        print("Response text:", response.text)
        return None

    breeds = data.get("message", {})
    names = []

    for breed, subbreeds in breeds.items():
        if subbreeds:
            for sub in subbreeds:
                names.append(f"{sub} {breed}")
        else:
            names.append(breed)

    # Print breeds with numbering
    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")

    # Convert list to dict with numbering as keys
    names_dict = {i: name for i, name in enumerate(names, 1)}
    return names_dict

breed_dict = dogbreedname()
print("\nDictionary form:")
print(breed_dict)


         






