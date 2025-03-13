from src.databases.database import database
from src.models.post_model import posts
from src.schemas.post_schema import PostIn, PostUpdate
from src.views.post_view import PostOut


class PostService:
    @staticmethod
    async def read_post(id: int):
        post = posts.select().where(posts.c.id == id)
        post = await database.fetch_one(post)

        return post if post else None

    @staticmethod
    async def read_posts(
        skip: int, limit: int, published: bool
    ) -> list[PostOut] | None:
        list_posts = (
            posts.select()
            .where(posts.c.id > skip)
            .where(posts.c.published == published)
            .limit(limit)
        )
        list_posts = await database.fetch_all(list_posts)

        return list_posts if list_posts else None

    @staticmethod
    async def insert_post(post: PostIn) -> int:
        statement = posts.insert().values(**post.model_dump())
        id = await database.execute(statement)

        return id

    @staticmethod
    async def change_post(id: int, post: PostUpdate) -> None:
        post = post.model_dump(exclude_unset=True)
        statement = posts.update().where(posts.c.id == id).values(**post)
        await database.execute(statement)

        return

    @staticmethod
    async def remove_post(id: int) -> None:
        statement = posts.delete().where(posts.c.id == id)
        await database.execute(statement)

        return
