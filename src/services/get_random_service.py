from src.infra.database.repositories.random_repository import RandomRepository
from src.providers.random_provider import RandomProvider


class GetRandomService:
  def __init__(
    self,
    random_repository: RandomRepository,
    random_provider: RandomProvider,
  ):
    self.random_repository = random_repository
    self.random_provider = random_provider

  def execute(self) -> dict:
    item = self.random_repository.get_default_item()

    return {
      "id": item["id"],
      "name": item["name"],
      "message": self.random_provider.build_message(item["name"]),
    }