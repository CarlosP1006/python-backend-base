from dependency_injector import containers, providers

from src.infra.database.repositories.random_repository import RandomRepository
from src.providers.random_provider import RandomProvider
from src.services.get_random_service import GetRandomService


class AppContainer(containers.DeclarativeContainer):
  random_provider = providers.Singleton(RandomProvider)
  random_repository = providers.Singleton(RandomRepository)

  get_random_service = providers.Singleton(
    GetRandomService,
    random_repository=random_repository,
    random_provider=random_provider,
  )


container = AppContainer()
