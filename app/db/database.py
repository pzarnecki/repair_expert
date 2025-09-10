from sqlmodel import create_engine, Session

engine = create_engine("sqlite:///./calc.db", echo=True)

def get_session():
    with Session(engine) as session:
        yield session