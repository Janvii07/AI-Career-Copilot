from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = (
    "mysql+pymysql://3KoKY3Krj22gfP3.root:oWShSq4lt7RNHSon@"
    "gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {"ca": "C:/Users/janvi/OneDrive/Desktop/AI_Career_copilot/ca.pem"}
    }
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
