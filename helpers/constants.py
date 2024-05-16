class SqlQueries:
    CREATE_AUTH = """
        CREATE TABLE `auth` (
            `id` varchar(255),
            `email` varchar(255) NOT NULL,
            `username` varchar(255) NOT NULL,
            `hash_password` varchar(255) NOT NULL,
            PRIMARY KEY (`id`),
            UNIQUE KEY `email` (`email`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
    """

    CREATE_RECOMMENDATION_TABLE = """
        CREATE TABLE `recommendation_history` (
            `id` char(36) NOT NULL,
            `user_id` int DEFAULT NULL,
            `song_name` varchar(255) DEFAULT NULL,
            `album_name` varchar(255) DEFAULT NULL,
            `artist_name` varchar(255) DEFAULT NULL,
            `release_year` int DEFAULT NULL,
            `ratings` float DEFAULT NULL,
            `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
    """

    SIGN_UP = """
        INSERT INTO auth
        VALUES (%s, %s, %s, %s);
    """

    SIGN_IN = """
        SELECT * FROM auth
        WHERE email = %s;
    """

    INSERT_RECOMMENDED_SONGS = """
        INSERT INTO recommendation_history (id, user_id, song_name, album_name, artist_name, release_year, ratings)
        VALUES (%s, %s, %s, %s, %s);
    """

    GET_USER_HISTORY = """
        SELECT * FROM recommendation_history
        WHERE user_id = %s;
    """

    GET_ALL_USERS = """
        SELECT * FROM auth;
    """

    GET_ALL_RECOMMENDED_SONGS = """
        SELECT * FROM recommendation_history;
    """


class Strings:
    PROMPT = """
        Suggest me 20 songs with having these genres {}, moods {}, languages {}
        in json format
        containing a key songs which will have a list of object
        which contains song_name, album_name, artist_name, release_year, ratings
    """

    AND = "and"
    CHOICES = "choices"
    TEXT = "text"
    SONGS = "songs"
    SONG_NAME = "song_name"
    MOVIE_NAME = "movie_name"
    ARTIST_NAME = "artist_name"
