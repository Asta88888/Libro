import requests


def get_coordinates(address: str):
    """
    Получает координаты по адресу через OpenStreetMap (Nominatim).
    """

    if not address:
        return None, None

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": address,
        "format": "json",
        "limit": 1,
    }

    headers = {
        "User-Agent": "LibroApp"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=5,
        )

        response.raise_for_status()

        data = response.json()

        if data:
            return (
                float(data[0]["lat"]),
                float(data[0]["lon"])
            )

        return None, None

    except requests.RequestException as e:
        print(f"Geocoding error: {e}")

    return None, None