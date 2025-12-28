from dataclasses import dataclass

import polars as pl
from .engine.game_graph import GameGraph

@dataclass
class GameConfig:
    """
    Game configuration dataclass

    :param difficulty: Difficulty of the game
    """
    difficulty: int


class Game:

    film_df = pl.scan_parquet("game_data/film_dataset.parquet")
    actor_df = pl.scan_parquet("game_data/film_actors.parquet")

    def __init__(self, config: GameConfig) -> None:
        """ The main game class. """

        self.game_graph = GameGraph(film_df=self.film_df, actor_df=self.actor_df)

        self.game_graph.current_film = "Fight Club"

    def check_film_link(self, film_name: str):
        links = self.game_graph.get_film_links(film_name)

        if links.is_empty():
            return False

        else:
            print(f"Found links on {links.get_column("actors")}")
            return True

    def run(self):
        ...


if __name__ == "__main__":
    game = Game(GameConfig(difficulty=1))
    game.check_film_link("Mr. & Mrs. Smith")