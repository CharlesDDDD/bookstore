from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
<<<<<<< HEAD
engine = create_engine('mysql+pymysql://root:cui,logic@127.0.0.1:3306/test', convert_unicode=True)
=======
engine = create_engine('mysql+pymysql://root:WAMM0609dd@localhost:3306/test', convert_unicode=True)
>>>>>>> f88bb057c0c45671fee6aa62904425ee4dc1a834
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # 在这里导入定义模型所需要的所有模块，这样它们就会正确的注册在
    # 元数据上。否则你就必须在调用 init_db() 之前导入它们。
    import be.table.user
    import be.table.store
    import be.table.user_store
    import be.table.new_order_detail
    import be.table.new_order

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
<<<<<<< HEAD
=======
    # from be.table.book import BookDB
    # bookdb=BookDB()
    # bookdb.get_book_info(0,bookdb.get_book_count())
>>>>>>> f88bb057c0c45671fee6aa62904425ee4dc1a834


init_db()
