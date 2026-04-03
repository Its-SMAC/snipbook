from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///snipbook.db")

def main() -> None:
    with engine.connect() as conn:
        result = conn.execute(text("select 'hello world'"))
        print(result.all())


if __name__ == '__main__':
    main()
