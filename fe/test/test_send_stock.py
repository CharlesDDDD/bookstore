import pytest

from fe.access.book import Book
from fe.test.gen_book_data import GenBook
from fe.access.new_buyer import register_new_buyer
import uuid
class TestSendStock:
    @pytest.fixture(autouse=True)
    def pre_run_initialization(self):
        self.seller_id = "test_send_seller_id_{}".format(str(uuid.uuid1()))
        self.store_id = "test_send_store_id_{}".format(str(uuid.uuid1()))
        self.buyer_id = "test_send_buyer_id_{}".format(str(uuid.uuid1()))
        self.password = self.seller_id
        gen_book = GenBook(self.seller_id, self.store_id)
        self.seller=gen_book.seller
        ok, buy_book_id_list = gen_book.gen(non_exist_book_id=False, low_stock_level=False, max_book_count=5)
        self.buy_book_info_list = gen_book.buy_book_info_list
        assert ok
        b = register_new_buyer(self.buyer_id, self.password)
        self.buyer = b

        code, self.order_id = b.new_order(self.store_id, buy_book_id_list)
        print(self.order_id)
        assert code == 200

        self.total_price = 0
        for item in self.buy_book_info_list:
            book: Book = item[0]
            num = item[1]
            if book.price is None:
                continue
            else:
                self.total_price = self.total_price + book.price * num
        yield

    def test_ok(self):
        code = self.buyer.add_funds(self.total_price)
        assert code == 200
        code = self.buyer.payment(self.order_id)
        assert code == 200
        code = self.seller.send_stock(self.seller_id,self.order_id)
        assert code ==200
