from be.table.user import User
from be.table.user_store import User_Store
from be.table.store import Store


class DBConn:

    def user_id_exist(self,user_id):
        row = User.query.filter(User.user_id == user_id).first()
        if row is None:
            return False
        else:
            return True

    def book_id_exist(self,store_id, book_id):
        row = Store.query.filter(Store.store_id == store_id, Store.book_id == book_id).first()
        if row is None:
            return False
        else:
            return True

    def store_id_exist(self,store_id):
        row = User_Store.query.filter(User_Store.store_id == store_id).first()
        if row is None:
            return False
        else:
            return True
