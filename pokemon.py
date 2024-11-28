import pandas as pd

class Pokemon:
    def __init__(self, name, p_type, attack, defense, stamina):
        self.name = name
        self.type = p_type
        self.attack = attack
        self.defense = defense
        self.stamina = stamina

    def __str__(self):
        return f"{self.name} ({self.type}): ATK {self.attack}, DEF {self.defense}, STA {self.stamina}"

class PokemonManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.pokemons = self.load_pokemons()

    def load_pokemons(self):
        data = pd.read_csv(self.csv_file)
        return [Pokemon(row['name'], row['type'], row['attack'], row['defense'], row['stamina']) for index, row in data.iterrows()]

    def add_pokemon(self, name, p_type, attack, defense, stamina):
        new_pokemon = Pokemon(name, p_type, attack, defense, stamina)
        self.pokemons.append(new_pokemon)
        self.save_pokemons()

    def modify_pokemon(self, name, new_pokemon):
        for i, pokemon in enumerate(self.pokemons):
            if pokemon.name == name:
                self.pokemons[i] = new_pokemon
                self.save_pokemons()
                return
        print(f"Pokémon {name} no encontrado.")

    def delete_pokemon(self, name):
        self.pokemons = [pokemon for pokemon in self.pokemons if pokemon.name != name]
        self.save_pokemons()

    def save_pokemons(self):
        data = [{'name': p.name, 'type': p.type, 'attack': p.attack, 'defense': p.defense, 'stamina': p.stamina} for p in self.pokemons]
        df = pd.DataFrame(data)
        df.to_csv(self.csv_file, index=False)

    def battle(self, name1, name2):
        p1 = next((p for p in self.pokemons if p.name == name1), None)
        p2 = next((p for p in self.pokemons if p.name == name2), None)
        
        if p1 is None or p2 is None:
            print(f"No se encontraron ambos pokémons: {name1} y/o {name2}.")
            return

        print(f"¡Comienza la batalla entre {p1.name} y {p2.name}!")
        
        if (p1.attack + p1.defense + p1.stamina) > (p2.attack + p2.defense + p2.stamina):
            print(f"El ganador es {p1.name}!")
        else:
            print(f"El ganador es {p2.name}!")

def main():
    manager = PokemonManager('pokemon.csv')
    
    # Agrega un nuevo pokémon
    manager.add_pokemon('Eevee', 'Normal', 55, 50, 55)
    
    # Modifica un pokémon existente
    manager.modify_pokemon('Pikachu', Pokemon('Pikachu', 'Electric', 60, 45, 40))
    
    # Elimina un pokémon
    manager.delete_pokemon('Jigglypuff')
    
    # Simula una batalla
    manager.battle('Pikachu', 'Charmander')

if __name__ == '__main__':
    main()
