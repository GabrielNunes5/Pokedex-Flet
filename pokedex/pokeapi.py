import requests


def get_pokemon(pokemon: str):
    # Link da api + criando reponse
    api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'.lower()
    response = requests.get(api_url).json()

    pokemon_name = response.get("name").capitalize()
    pokemon_img = response.get("sprites", {}).get(
        "other").get("showdown").get("front_default")
    pokemon_id = response.get("id")
    pokemon_types = [ptype["type"]["name"].capitalize()
                     for ptype in response.get("types", [])]
    pokemon_weight = response.get("weight")
    pokemon_hp = response.get("stats")[0].get("base_stat")
    pokemon_attack = response.get("stats")[1].get("base_stat")
    pokemon_defense = response.get("stats")[2].get("base_stat")
    pokemon_special_attack = response.get("stats")[3].get("base_stat")
    pokemon_special_defense = response.get("stats")[4].get("base_stat")
    pokemon_speed = response.get("stats")[5].get("base_stat")
    if pokemon_id <= 151:
        pokemon_gen = "1ª Geração"
    elif pokemon_id <= 251:
        pokemon_gen = "2ª Geração"
    elif pokemon_id <= 386:
        pokemon_gen = "3ª Geração"
    elif pokemon_id <= 493:
        pokemon_gen = "4ª Geração"
    elif pokemon_id <= 649:
        pokemon_gen = "5ª Geração"
    elif pokemon_id <= 721:
        pokemon_gen = "6ª Geração"
    elif pokemon_id <= 809:
        pokemon_gen = "7ª Geração"
    elif pokemon_id <= 898:
        pokemon_gen = "8ª Geração: Galar"
    elif pokemon_id <= 905:
        pokemon_gen = "8ª Geração: Hisui"
    else:
        pokemon_gen = "9ª Geração"

    pokemon_data = [pokemon_img,
                    pokemon_name,
                    pokemon_id,
                    pokemon_types,
                    pokemon_weight,
                    pokemon_hp,
                    pokemon_attack,
                    pokemon_defense,
                    pokemon_special_attack,
                    pokemon_special_defense,
                    pokemon_speed,
                    pokemon_gen,
                    ]
    return pokemon_data


# print(get_pokemon("Deoxys Velocidade"))
