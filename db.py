from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

user_name = "root"
password = "password"
server = "127.0.0.1"
port = 3306
db_name = "todo_app"

url_database = f"mysql+pymysql://{user_name}:{password}@{server}:{port}/{db_name}"


def get_engine():
    try:
        engine = create_engine(url_database)
        metadata = MetaData()
        metadata.reflect(bind=engine)

        Base = automap_base(metadata=metadata)
        Base.prepare()

        Session = sessionmaker(bind=engine)
        session = Session()

        return session, Base
    except OperationalError:
        print("Error with the database connection...❌")
        session = None
        Base = None
        return session, Base
