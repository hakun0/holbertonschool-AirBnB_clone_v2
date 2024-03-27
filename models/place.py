
#!/usr/bin/python3
""" Place Module for HBNB project"""
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             overlaps="place_amenities", viewonly=False)

    """if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            "returns the list of Review instances"
            review_list = []
            all_review = models.storage.all(Review)
            for review in all_review.values():
                if self.id == review.place_id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            "returns the list of Amenity instances"
            new_list = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.place_id == self.id:
                    new_list.append(amenity)
            return new_list

        @amenities.setter
        def amenities(self, obj):
            if type(obj) == Amenity:
                self.amenity_ids.appends(obj.id)"""
