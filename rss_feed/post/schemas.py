from marshmallow import Schema, fields
from sqlalchemy import DateTime


class BasePostSchema(Schema):
    """Basic layout for Posts."""
    id: int = fields.Int()
    name: str = fields.Str()
    created_at: DateTime = fields.DateTime()
    updated_at: DateTime = fields.DateTime()
    short_description: str = fields.Str()


class CreatePostSchema(BasePostSchema):
    """Scheme for creating posts."""
    content = fields.Str()


class DetailPostSchema(CreatePostSchema):
    """Schema for getting detail of post."""


class ListPostSchema(BasePostSchema):
    """Scheme for getting posts."""
