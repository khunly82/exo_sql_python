# Setup alembic

## Installer Alembic

```sh
pip install alembic
```

## Configurer Alembic

1. Initialiser Alembic (dossier alembic + fichier alembic.ini)

```sh
alembic init alembic
```

2. Modification de alembic.ini pour ajouter l'url de connection

*Dans le fichier alembic.ini modifier*

```
sqlalchemy.url = driver://user:pass@host:port/dbname
```

3. Importer les metadata (alembic/env.py)

```python
import sys
from os.path import abspath, dirname, join
sys.path.insert(0, abspath(join(dirname(__file__), '..', 'src')))
from models import Base

target_metadata = Base.metadata
```

## Migrations

- Ajouter une revision vide

```sh
alembic revision -m "description de la révision"
```

- Ajouter une revision en se basant sur les modifications des models

```sh
alembic revision --autogenerate -m "description de la révision"
```

- Mettre à jour la db

```sh
alembic upgrade head
# ou
alembic upgrade <version>
# ou
alembic downgrade <version>
```

