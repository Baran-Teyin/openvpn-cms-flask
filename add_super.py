from lin.core import User
from lin.db import db

from app.app import create_app


def main():
    app = create_app()
    with app.app_context():
        with db.auto_commit():
            # 创建一个超级管理员
            user = User()
            user.username = 'super'
            user.password = 'openvpn@123456'
            user.email = 'hello_openvpn@163.com'
            # admin 2 的时候为超级管理员，普通用户为 1
            user.admin = 2
            db.session.add(user)


if __name__ == '__main__':
    try:
        main()
        print("新增超级管理员成功")
    except Exception as e:
        raise e
