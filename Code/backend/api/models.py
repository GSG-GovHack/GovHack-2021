from uuid import uuid4, UUID
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from mongoengine import Document, ListField, StringField, MultiPolygonField, DateTimeField, UUIDField, ReferenceField, CASCADE, GeoPointField, IntField


#########
# Enums #
#########
class PublicSpaceTypes(str, Enum):
    park = "park"


class ReportTypes(str, Enum):
    lighting = "lighting"
    rubbish = "rubbish"


###############
# Marshalling #
###############
class PlacesListIn(BaseModel):
    place_id: UUID
    lat: float
    lon: float


class PublicSpaceIn(BaseModel):
    name: str
    type: PublicSpaceTypes
    bounds: List[List[List]]


class ReportIn(BaseModel):
    type: ReportTypes
    public_space: UUID


class PublicFeedbackIn(BaseModel):
    lighting_rating: int
    safety_rating: int
    comments: str


class UserIn(BaseModel):
    name: str
    username: str
    email: EmailStr


#############
# DB Models #
#############
class User(Document):
    """User document"""
    id = UUIDField(default=uuid4, primary_key=True)
    name = StringField(required=True)
    username = StringField(required=True)
    email = StringField(required=True)
    points = IntField()


class PublicSpace(Document):
    """MongoDB Document for storing a place/public space"""
    id = UUIDField(null=False, primary_key=True, default=uuid4)
    name = StringField(required=True)
    type = StringField(required=True)
    bounds = MultiPolygonField(required=True)
    ts = DateTimeField(required=True, default=datetime.now)
    meta = {
        'indexes': [[("bounds", "2dsphere")]]
    }


class PublicReport(Document):
    """MongoDB Document for storing reports by users (rubbish, covid, etc)"""
    id = UUIDField(null=False, primary_key=True, default=uuid4)
    user = ReferenceField(User, reverse_delete_rule=CASCADE)
    place = ReferenceField(PublicSpace, reverse_delete_rule=CASCADE)
    # Data
    type = StringField(required=True)
    ts = DateTimeField(required=True, default=datetime.now)


class PublicFeedback(Document):
    """MongoDB Document for storing feedback about the specified place"""
    #user = ReferenceField(User, reverse_delete_rule=CASCADE)
    id = UUIDField(null=False, primary_key=True, default=uuid4)
    place = ReferenceField(PublicSpace, reverse_delete_rule=CASCADE)
    # Data
    lighting_rating = IntField(required=True)
    safety_rating = IntField(required=True)
    comments = StringField(required=True)
    ts = DateTimeField(required=True, default=datetime.now)
