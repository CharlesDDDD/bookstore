from be.table.User import User
from be.table.User_Store import User_Store
from be.table.Store import Store


class DBConn:

    def user_id_exist(self, user_id: str):
        row = User.query.filter(User.user_id == user_id).first()
        if row is None:
            return False
        else:
            return True

    def book_id_exist(self, store_id, book_id):
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
