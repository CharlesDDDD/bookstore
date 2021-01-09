import sqlite3 as sqlite
import uuid
import json
import logging
from be.model import db_conn
from be.model import error
from be.table.new_order import New_Order
from be.table.new_order_detail import New_Order_Detail
from be.table.user import User
from be.table.store import Store
from be.table.user_store import User_Store
from be.model.database import db_session

class Buyer(db_conn.DBConn):
    def __init__(self):
        db_conn.DBConn.__init__(self)

    def new_order(self, user_id: str, store_id: str, id_and_count: [(str, int)]) -> (int, str, str):
        order_id = ""
        try:
            if not self.user_id_exist(user_id):
                return error.error_non_exist_user_id(user_id) + (order_id, )
            if not self.store_id_exist(store_id):
                return error.error_non_exist_store_id(store_id) + (order_id, )
            uid = "{}_{}_{}".format(user_id, store_id, str(uuid.uuid1()))
            print(uid)


            for book_id, count in id_and_count:

                # cursor = self.conn.execute(
                #     "SELECT book_id, stock_level, book_info FROM store "
                #     "WHERE store_id = ? AND book_id = ?;",
                #     (store_id, book_id))
                row=Store.query.filter_by(store_id=store_id,book_id=book_id).first()

                if row is None:
                    return error.error_non_exist_book_id(book_id) + (order_id, )

                stock_level = row.stock_level
                book_info = row.book_info
                book_info_json = json.loads(book_info)
                price = book_info_json.get("price")

                if stock_level < count:
                    return error.error_stock_level_low(book_id) + (order_id,)

                # cursor = self.conn.execute(
                #     "UPDATE store set stock_level = stock_level - ? "
                #     "WHERE store_id = ? and book_id = ? and stock_level >= ?; ",
                #     (count, store_id, book_id, count))
                row=Store.query.filter_by(store_id=store_id,book_id=book_id,stock_level=stock_level).update({'stock_level':stock_level-count})
                if row == 0:
                    return error.error_stock_level_low(book_id) + (order_id, )

                # self.conn.execute(
                #         "INSERT INTO new_order_detail(order_id, book_id, count, price) "
                #         "VALUES(?, ?, ?, ?);",
                #         (uid, book_id, count, price))
                row=New_Order_Detail(order_id=uid,book_id=book_id,count=count,price=price)
                db_session.add(row)

            # self.conn.execute(
            #     "INSERT INTO new_order(order_id, store_id, user_id) "
            #     "VALUES(?, ?, ?);",
            #     (uid, store_id, user_id))
            # self.conn.commit()
            row=New_Order(order_id=uid,store_id=store_id,user_id=user_id)
            db_session.add(row)
            order_id = uid
            db_session.commit()

        # except sqlite.Error as e:
        #     logging.info("528, {}".format(str(e)))
        #     return 528, "{}".format(str(e)), ""
        except BaseException as e:
            logging.info("530, {}".format(str(e)))
            return 530, "{}".format(str(e)), ""

        return 200, "ok", order_id

    def payment(self, user_id: str, password: str, order_id: str) -> (int, str):
        try:
            # cursor = conn.execute("SELECT order_id, user_id, store_id FROM new_order WHERE order_id = ?", (order_id,))
            # row = cursor.fetchone()
            print(user_id,order_id,password)

            row=New_Order.query.filter_by(order_id=order_id).first()
            if row is None:
                return error.error_invalid_order_id(order_id)
            order_id = row.order_id
            buyer_id = row.user_id
            store_id = row.store_id
            print(order_id,buyer_id,store_id)

            if buyer_id != user_id:
                return error.error_authorization_fail()

            # cursor = conn.execute("SELECT balance, password FROM user WHERE user_id = ?;", (buyer_id,))
            # row = cursor.fetchone()
            row=User.query.filter_by(user_id=buyer_id).first()

            if row is None:
                return error.error_non_exist_user_id(buyer_id)
            balance = row.balance
            if password != row.password:
                return error.error_authorization_fail()

            # cursor = conn.execute("SELECT store_id, user_id FROM user_store WHERE store_id = ?;", (store_id,))
            # row = cursor.fetchone()
            #买家
            row=User_Store.query.filter_by(store_id=store_id).first()
            if row is None:
                return error.error_non_exist_store_id(store_id)

            seller_id = row.user_id
            #卖家
            row=User.query.filter_by(user_id=seller_id).first()
            if row is None:
                return error.error.error_non_exist_user_id(seller_id)
            seller_balance=row.balance

            if not self.user_id_exist(seller_id):
                return error.error_non_exist_user_id(seller_id)

            # cursor = conn.execute("SELECT book_id, count, price FROM new_order_detail WHERE order_id = ?;", (order_id,))
            cursor=New_Order_Detail.query.filter_by(order_id=order_id).all()
            total_price = 0
            for row in cursor:
                count = row.count
                price = row.price
                total_price = total_price + price * count

            #买家付钱，钱减少
            if balance < total_price:
                return error.error_not_sufficient_funds(order_id)
            # cursor = conn.execute("UPDATE user set balance = balance - ?"
            #                       "WHERE user_id = ? AND balance >= ?",
            #                       (total_price, buyer_id, total_price))
            cursor=User.query.filter(User.user_id==buyer_id,User.balance>=total_price).update({'balance':balance-total_price})

            if cursor == 0:
                return error.error_not_sufficient_funds(order_id)

            # cursor = conn.execute("UPDATE user set balance = balance + ?"
            #                       "WHERE user_id = ?",
            #                       (total_price, buyer_id))
            #卖家付钱，钱增多
            cursor=User.query.filter_by(user_id=seller_id).update({'balance':seller_balance+total_price})
            if cursor == 0:
                return error.error_non_exist_user_id(seller_id)

            # cursor = conn.execute("DELETE FROM new_order WHERE order_id = ?", (order_id, ))
            cursor=New_Order.query.filter_by(order_id=order_id).delete()
            if cursor == 0:
                return error.error_invalid_order_id(order_id)

            #删除订单记录
            # cursor = conn.execute("DELETE FROM new_order_detail where order_id = ?", (order_id, ))
            cursor = New_Order_Detail.query.filter_by(order_id=order_id).delete()
            if cursor == 0:
                return error.error_invalid_order_id(order_id)

            db_session.commit()

        # except sqlite.Error as e:
        #     return 528, "{}".format(str(e))

        except BaseException as e:
            return 530, "{}".format(str(e))

        return 200, "ok"

    def add_funds(self, user_id:str, password:str, add_value:int) -> (int, str):
        try:
            # cursor = self.conn.execute("SELECT password  from user where user_id=?", (user_id,))
            # row = cursor.fetchone()
            row=User.query.filter_by(user_id=user_id).first()
            if row is None:
                return error.error_authorization_fail()

            if row.password != password:
                return error.error_authorization_fail()
            balance=row.balance

            # cursor = self.conn.execute(
            #     "UPDATE user SET balance = balance + ? WHERE user_id = ?",
            #     (add_value, user_id))
            cursor=User.query.filter_by(user_id=user_id).update({"balance":balance+add_value})
            if cursor == 0:
                return error.error_non_exist_user_id(user_id)

            db_session.commit()
            # self.conn.commit()
        # except sqlite.Error as e:
        #     return 528, "{}".format(str(e))
        except BaseException as e:
            return 530, "{}".format(str(e))

        return 200, "ok"
