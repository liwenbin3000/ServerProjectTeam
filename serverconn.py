import pymysql
import time


class serverconn:
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         passwd='12345',
                         db='p',
                         charset='utf8')

    cursor = db.cursor()

    # 插入语句方法
    # 向product表插入数据

    # 向suppiler表插入数据
    def insertsupplier(self, sname, saddr, stele, speople, sphone):
        sql = "INSERT INTO supplier(sname,saddr,stele,speople,sphone) values('" + sname + "','" + saddr + "','" + stele + "','" + speople + "','" + sphone + "')"
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            return 1
        return 0

    # 向buyer表插入数据
    def insertbuyer(self, bname, baddr, btele, bpeople, bphone):
        sql = "INSERT INTO buyer(bname,baddr,btele,bpeople,bphone) values('" + bname + "','" + baddr + "','" + btele + "','" + bpeople + "','" + bphone + "')"
        print(sql)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            return 1
        return 0

    # 向debt表插入数据
    def insertdebt(self, dtime, pno, bno, buynum, bill):
        sql = "INSERT INTO debt(dtime,pno,bno,buynum,bill) values('" + dtime + "'," + str(pno) + "," + str(
            bno) + "," + str(buynum) + "," + str(bill) + ")"
        print(sql)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            return 1
        return 0

    # 向debt1表插入数据
    def insertdebt1(self, dtime, pno, sno, sellnum, bill):
        sql = "INSERT INTO debt1(dtime,pno,sno,sellnum,bill) values('" + dtime + "'," + str(pno) + "," + str(
            sno) + "," + str(sellnum) + "," + str(bill) + ")"
        print(sql)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            return 1
        return 0

    # 查询语句

    # 删除语句


x = serverconn()
# x.insertproduct("s222","sdsad",156,546)
# x.insertsupplier("苹果","杭州","1354548513","lisiaj","354651351351")
# x.insertbuyer("sdlno","sadasodowa","312356","saasdas","326+5+62")
# x.insertdebt("xsdsdfs",1,1,51516,5135)
#  x.insertdebt1("xsdsdfs",1,1,51516,5135)
