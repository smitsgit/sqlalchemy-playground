from repo.database import engine
from repo import models


def main():
    # For creating the schema models need to be imported first
    models.SqlAlchemyBase.metadata.create_all(engine)


if __name__ == '__main__':
    main()
