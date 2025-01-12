from python-decouple import config
import Flask
import Bcrypt
from flask_migrate import Migrate
import SQLAlchemy
from src.accounts.views import accounts_bp
from src.core.views import core_bp

app = Flask(__name__)

app.config.from_object(config("APP_SETTINGS"))

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)