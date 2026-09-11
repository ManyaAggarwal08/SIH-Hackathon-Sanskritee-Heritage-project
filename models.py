from sqlalchemy import Column, Integer, String, Text
from database import Base

class Place(Base):
    __tablename__ = "places"
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    best_time_to_visit = Column(Text)
    mythological_importance = Column(Text)
    historical_importance = Column(Text)
    heritage_info = Column(Text)
    culture_tradition = Column(Text)
    fun_facts_stories = Column(Text)
    atmosphere_vibe = Column(Text)
    location = Column(Text)
