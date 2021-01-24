# -*- coding: UTF-8 -*-
# Public package
import threading
# Private package
import default as default
import headpy.hbes.hnew as hnew

################################################################################
# dump常规root文件
dump_real = 0
dump_pppmpz = 0
dump_pppmpz_truth = 1
dump_back_back = 0
dump_pwa = 0
dump_pwa_truth = 0
################################################################################


class mythread(threading.Thread):
    def __init__(self, location, tree, branchs, tree_cut):
        threading.Thread.__init__(self)
        self.location = location
        self.tree = tree
        self.branchs = branchs
        self.tree_cut = tree_cut

    def run(self):
        print('开始线程: %s' % (self.location))
        hnew.dump(default.root_dict,
                  folder_root=self.location,
                  tree=self.tree,
                  branchs=self.branchs,
                  tree_cut=self.tree_cut)
        print('结束线程: %s' % (self.location))


# 输入文件地址
massages = hnew.massage_read()
location1 = '%s' % (massages['real'])
location2 = '%s' % (massages['pppmpz'])
location3 = '%s' % (massages['back_back'])
location4 = '%s' % (massages['pwa'])
# 创建进程
thread1 = mythread(location1, 'fit4c', default.branchs_fit4c, 1)
thread2 = mythread(location2, 'fit4c', default.branchs_fit4c_truth, 1)
thread3 = mythread(location2, 'truth', default.branchs_truth, 0)
thread4 = mythread(location3, 'fit4c', default.branchs_fit4c, 1)
thread5 = mythread(location4, 'fit4c', default.branchs_fit4c, 1)
thread6 = mythread(location4, 'truth', default.branchs_truth, 0)
# 开始进程
if(dump_real == 1):
    thread1.start()
if(dump_pppmpz == 1):
    thread2.start()
if(dump_pppmpz_truth == 1):
    thread3.start()
if(dump_back_back == 1):
    thread4.start()
if(dump_pwa == 1):
    thread5.start()
if(dump_pwa_truth == 1):
    thread6.start()
# 停止进程
if(dump_real == 1):
    thread1.join()
if(dump_pppmpz == 1):
    thread2.join()
if(dump_pppmpz_truth == 1):
    thread3.join()
if(dump_back_back == 1):
    thread4.join()
if(dump_pwa == 1):
    thread5.join()
if(dump_pwa_truth == 1):
    thread6.join()
