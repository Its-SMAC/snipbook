from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///snipbook.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)


class Base(declarative_base()):
    pass

def create_tables():
    Base.metadata.create_all(engine)

def main() -> None:
    pass


if __name__ == '__main__':
    main()
