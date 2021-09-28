from app import factory, db
from flask_migrate import Migrate

from app.models import Ususarios

app = factory()
migrate = Migrate (app, db)

@app.shell_context_processor
def shell():
    return dict(
        db=db,
        Ususarios=Ususarios
    )