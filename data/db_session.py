from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SqlAlchemyBase = declarative_base()

__factory = None


def global_init(db_file=None):
    global __factory
    if __factory:
        return

    if not db_file:
        raise Exception("Необходимо задать путь к файлу базы данных.")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключаемся к базе данных по адресу {conn_str}")

    engine = create_engine(conn_str, echo=False)
    __factory = sessionmaker(bind=engine)

    from .models import users_model

    SqlAlchemyBase.metadata.create_all(engine)


def create_session():
    global __factory
    return __factory()