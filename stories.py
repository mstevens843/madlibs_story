"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

superhero_tale = Story(
    ["superhero_name", "city", "villain", "superpower", "verb"],
    """In the city of {city}, {superhero_name} faced their greatest foe, {villain}.
    Using their {superpower}, they managed to {verb} and save the day!"""
)

fairytale = Story(
    ["name", "adjective", "creature", "place", "verb"],
    """Once upon a time, {name} the {adjective} {creature} ventured into the {place}.
    There, they bravely attempted to {verb} their way to victory."""
)


wild_west = Story(
    ["cowboy_name", "town", "adjective", "animal", "verb"],
    """Out in the dusty town of {town}, {cowboy_name} rode in on their trusty {animal}.
    The town was {adjective}, and the only thing left to do was {verb} their way out of trouble."""
)

# Dictionary of stories
stories = {
    "original": story,
    "fairytale": fairytale,
    "superhero_tale": superhero_tale,
    "wild_west": wild_west,
}
