class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        filtered = [p for p in self.pokemon if p.name == pokemon_name]
        if filtered:
            self.pokemon.remove(filtered[0])
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

        # if pokemon_name in self.pokemon:
        #     self.pokemon.remove(pokemon_name)
        #     return f"You have released {pokemon_name}"
        # return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        result += '\n'.join([f"- {p.pokemon_details()}" for p in self.pokemon])
        return result
