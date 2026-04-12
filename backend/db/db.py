from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker

url = URL.create(
    "postgresql+psycopg2",
    username="casaos",
    password="casaos",
    host="192.168.1.200",
    port=5432,
    database="SnipBook",
)

engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)


class Base(declarative_base()):
    pass

def create_tables():
    Base.metadata.create_all(engine)

def main() -> None:
    pass


if __name__ == '__main__':
    main()
