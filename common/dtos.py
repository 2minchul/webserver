from typing import Type, TypeVar

from pydantic import BaseModel, TypeAdapter, ConfigDict

T = TypeVar('T')


class ContextDto(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def from_dict(cls: Type[T], data: dict) -> T:
        return TypeAdapter(cls).validate_python(data)

    def to_dict(self) -> dict:
        return self.model_dump()
