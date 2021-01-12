import time

from be import serve
from be.model.database import db_session
from be.table.new_order_detail import New_Order_Detail


def auto_cancel():
    cursor = New_Order_Detail.query.filter_by(state=0).all()
        # 得到order_id_list
    order_id_list = []
    for item in cursor:
        order_id_list.append(item.order_id)
    order_id_list = list(set(order_id_list))  # 去重

    for id in order_id_list:
        row = New_Order_Detail.query.filter_by(order_id=id).first()
        end_time = time.time()
        print(end_time-row.time)
        if (end_time - row.time >= 600):  # 付款时间超过10分钟自动取消
            New_Order_Detail.query.filter_by(order_id=id).update({"state": -1})
            print("自动取消",id)
    db_session.commit()

if __name__ == "__main__":
    serve.be_run()
