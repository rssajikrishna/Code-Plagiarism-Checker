from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:manigandan@localhost/test"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session
from sqlalchemy.orm.session import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:manigandan@localhost/test"

engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()