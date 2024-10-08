from sqlalchemy.ext.asyncio import AsyncSession

from src.abstract_classes.abstract_unit_of_work import AbstractUnitOfWork
import src.repositories as repositories
from src.database.database import DataBase


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self._session_factory = DataBase().async_session_maker

    async def __aenter__(self):
        self.session: AsyncSession = self._session_factory()
        self.user = repositories.user_repository.UserRepository(self.session)
        self.product = repositories.product_repository.ProductRepository(self.session)
        self.image = repositories.image_repository.ImageRepository(self.session)
        self.category = repositories.category_repository.CategoryRepository(self.session)
        self.order = repositories.order_repository.OrderRepository(self.session)
        self.order_product = repositories.order_product_repository.OrderProductRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
