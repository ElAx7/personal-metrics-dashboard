from app.db.base import engine
from app.db.base import Base
from app.models_base import Metric

def init_db():
    # Create all tables in the database
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database initialized and tables created.")
