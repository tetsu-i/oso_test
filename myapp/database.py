from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy_bulk_lazy_loader import BulkLazyLoader

BulkLazyLoader.register_loader()

DATABASE = "mysql://root:password@127.0.0.1:3310/oso_test?charset=utf8"

engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=True,
    pool_recycle=600,
)

meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)
Base = declarative_base(metadata=meta)

UnauthSession: Session = sessionmaker(
    autocommit=False, autoflush=False, expire_on_commit=True, bind=engine
)


SessionForOso = sessionmaker(
    autocommit=False, autoflush=False, expire_on_commit=True, bind=engine
)
