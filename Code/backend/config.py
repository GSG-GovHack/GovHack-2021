
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="CLOVERAPI",
    settings_files=['settings.yaml', '.secrets.yaml'],
)
