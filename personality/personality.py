# personality.py

class Personality:
    def init(self):
        self.abilities = {
            "weather": WeatherAbility(),
            "email": EmailAbility(),
            "alarm": AlarmAbility(),
            # Add more abilities here
        }

    def respond(self, input_text):
        # Respond to user input using abilities
        for ability in self.abilities.values():
            if ability.can_handle(input_text):
                return ability.respond(input_text)
        return "I'm not sure what you mean"

    def get_ability(self, ability_name):
        # Get an ability by name
        return self.abilities.get(ability_name)

class Ability:
    def init(self):
