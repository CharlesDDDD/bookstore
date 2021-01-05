from be.model.database import db_session
from be.table.user import User

u = User(123, 231, 30,'sa', 'dsa')
db_session.add(u)
db_session.commit()


# from be.model.db_conn import DBConn
# a = DBConn.user_id_exist(user_id=0)
# print(a)