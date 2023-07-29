from sqlalchemy import create_engine, MetaData, table
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.automap import automap_base

user_name = "root"
password = "password"
server = "127.0.0.1"
port = 3306
db_name = "todo_app"

url_database = f"mysql+pymysql://{user_name}:{password}@{server}:{port}/{db_name}"

# Crea una instancia de Engine apuntando a tu base de datos MySQL:
engine = create_engine(url_database)

# Si ya tienes la bbdd creada perfectamente y quieres crear automáticamente los modelos

# Crea una instancia de MetaData y conecta el engine a ella:
metadata = MetaData()
metadata.reflect(bind=engine)

# Las genera automáticamente
Base = automap_base(metadata=metadata)
Base.prepare()

# Las genera manualmente y te permite tener mas control sobre tus modelos

# Crea una clase base para tus modelos utilizando declarative_base():
# Base = declarative_base()

# Define las clases de tus modelos automáticamente utilizando el diccionario metadata.tables:
# for table in metadata.tables.values():
#     class_name = table.name.capitalize()
#     model = type(class_name, (Base,), {'__tablename__': table.name, '__table__': table})
#     globals()[class_name] = model

# En este punto, tendrás clases de modelos generadas automáticamente que se corresponden con las tablas existentes en tu base de datos MySQL. Cada clase se llamará como el nombre de la tabla, con la primera letra en mayúscula, y tendrán la misma estructura y atributos que las tablas de la base de datos.

# Ahora puedes utilizar estas clases de modelos para interactuar con la base de datos utilizando SQLAlchemy de la manera que explicamos anteriormente. Por ejemplo:
Session = sessionmaker(bind=engine)
session = Session()

# Recuerda que esta aproximación de "ingesta de esquema" puede ser muy útil si ya tienes una base de datos existente y deseas generar los modelos de SQLAlchemy rápidamente. Sin embargo, ten en cuenta que los modelos generados automáticamente pueden requerir ajustes adicionales según tus necesidades específicas.
