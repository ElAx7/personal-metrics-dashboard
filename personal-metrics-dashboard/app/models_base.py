from app.db.base import Base
from sqlalchemy import Column, Integer, String, Float, Date

# Define the Metric model
class Metric(Base):
    __tablename__ = "metrics"

    # Define the columns for the Metric table
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(Date, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)
    value = Column(Float, nullable=False)
    note = Column(String, nullable=True)






