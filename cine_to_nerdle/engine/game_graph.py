import polars as pl


class GameGraph:
    """
    A graph of films where edges connect films that share actors.

    Attributes
    ----------
    joined_df : polars.LazyFrame
    current_film : str

    Methods
    -------
    traverse_from_film(film_tconst: str) -> list[str]
        Returns all films reachable from the given film in the graph.
    """
    def __init__(self, film_df: pl.LazyFrame, actor_df: pl.LazyFrame):
        self.joined_df = (
            film_df
            .join(actor_df, on="film_id", how="left")
            .group_by("film_id")
            .agg(
                pl.col("title").first(),
                pl.col("actor_name").drop_nulls().alias("actors")
            )
            .filter(
                pl.col("actors").list.len() > 0
            )
            .with_row_count("idx")
        )

        self.current_film = "Fight Club"

    def check_actor_link(self, actor_name: str):
        linked_actors = (
            self.joined_df
            .filter(
                pl.col("title") == self.current_film,
                pl.col("actors").list.contains(actor_name),
            )
            .explode(pl.col("actors"))
            .collect()
        )

        # print(linked_actors)

        return not linked_actors.is_empty()

    def get_film_links(self, film_title: str) -> pl.DataFrame:
        film_links = (
            self.joined_df
            .filter(
                (pl.col("title") == self.current_film) | (pl.col("title") == film_title)
            )
            .explode(pl.col("actors"))
            .select(pl.col("actors").value_counts())
            .unnest("actors")
            .filter(pl.col("count") > 1)
            .collect()
        )

        return film_links
