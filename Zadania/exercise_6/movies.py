def movie(title):
    """Fetch a movie title and check if it's on the list of movies

    :param str title: name of a movie
    :rtype: str
    :return: returns a message with text "favorite", "hated", or "no such movie"
    """
    movies = {
        "favourite": ["A New Hope", "Empire Strikes Back", "Return of the Jedi",
                      "The Force Awakens", "Jaws", "Predator", "Mad Max",
                      "Back to the Future", "2001: A Space Odyssey", "Robocop",
                      "The Hitchhiker's Guide to the Galaxy", "Doctor Who",
                      "Aliens", "Alien", "Terminator", "Blade Runner", "Matrix"],

        "hated": ["The Phantom Menace", "Attack of the Clones", "Star Trek",
                  "Alien Resurrection", "Twilight"]

    }

    is_favorite = 0
    is_hated = 0

    for key, values in movies.items():
        if key == "favourite":
            for movie in values:
                if movie == title:
                    is_favorite = 1
                    return key, is_favorite

        elif key == "hated":
            for movie in values:
                if movie == title:
                    is_hated = 1
                    return key, is_hated

    if is_favorite == 0 and is_hated == 0:
        return "no such movie", 0
