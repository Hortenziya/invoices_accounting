import os

import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv("config/config.env")

Base = sqlalchemy.orm.declarative_base()


class DataBaseEngine:
    def __init__(self) -> None:
        self.db_user = os.environ.get("DB_USER")
        self.db_password = os.environ.get("DB_PASSWORD")
        self.db_host = os.environ.get("DB_HOST")
        self.db_port = os.environ.get("DB_PORT", 5432)
        self.db_name = os.environ.get("DB_NAME")

        self._session_factory = self.configure()

    #створюємо двигун, створюємо yci таблиці,
    def configure(self):
        engine = create_engine(
            f"postgresql://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

        Base.metadata.create_all(engine)
        return sessionmaker(bind=engine)

    def get_session(self):
        return self._session_factory()


class MyTable(Base):
    __tablename__ = "mytable"
    id = Column(Integer, primary_key=True)
    account_number = Column(Integer)
    total = Column(Integer)
    details = Column(String)
    date_send = Column(DateTime)


class Information:
    def __init__(self) -> None:
        self.db = DataBaseEngine()

    def number_of_account(self):
        session = self.db.get_session()
        if session.query(MyTable).order_by(
            MyTable.account_number.desc(),
        ).first() is not None:
            last_record = session.query(MyTable).order_by(
                MyTable.account_number.desc()
            ).first()
            account_number = last_record.account_number
        else:
            account_number = 0
        return account_number

    def add_to_table(self, total, details, date, account_number):
        summary = MyTable(
            account_number=account_number,
            total=total,
            details=details,
            date_send=date,
        )
        session = self.db.get_session()
        session.add(summary)
        session.commit()
