from src.infra.database.entities.random_item import RandomItem


class RandomRepository:
  def get_default_item(self) -> RandomItem:
    return {
      "id": 1,
      "name": "python-backend-base",
    }