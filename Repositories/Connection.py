from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connection:
    def __init__(self, connection_string: str = "sqlite:///:memory:"):
        # self.engine = create_engine(connection_string, echo=True)
        self.engine = create_engine(connection_string, echo=True)
        self.session = sessionmaker(bind=self.engine)

    @contextmanager
    def use_session(self):
        session = self.session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
