import sqlalchemy as sa
import sqlalchemy.ext.declarative as dec
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init(db_file) -> None:
    """
    Принимает на вход адрес базы данных, затем проверяет, не создали ли мы уже фабрику подключений
     (то есть не вызываем ли мы функцию не первый раз).
     Если уже создали, то завершаем работу, так как начальную инициализацию надо проводить только единожды.
    """
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    """Осуществляет получение сессии подключения к базе данных."""
    global __factory
    return __factory()