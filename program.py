from repo.models import *
from repo.database import SessionLocal, engine
from repo.models import *


def main():
    session = SessionLocal()
    user = User(name="Don", full_name="Smital Desai", nick_name="Whats up", age=20)
    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()
