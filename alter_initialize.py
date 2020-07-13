from repo.database import engine
from repo import models  # This might look like an unused import but its necessary
from repo.base import SqlAlchemyBase


def main():
    # For creating the schema models need to be imported first
    # If you skip the import, the schema generation doesn't work
    # Note: Also wont work if you first import SqlAlchemyBase and then import models
    SqlAlchemyBase.metadata.create_all(engine)


if __name__ == '__main__':
    main()
