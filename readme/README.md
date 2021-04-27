# Maneu
聪少的订单管理系统
# manage
manage.py collectstatic 收集静态文件
# uwsgi
uwsgi --ini uwsgin.ini  启动
uwsgi --reload uwsgi/uwsgi.pid  重载
uwsgi --stop uwsgi/uwsgi.pid  停止
uwsgi --connect-and-read uwsgi/uwsgi.status  查看状态
