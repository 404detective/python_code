import matplotlib.pyplot as plt
import random
class pid(object):
    def __init__(self,exp_val,p,i,d):
        self.exp_val=exp_val
        self.kp=p
        self.ki=i
        self.kd=d
        self.now_err=0#现在误差
        self.last_err=0#上一次误差
        self.now_val=1000#现在值
        self.sum_err=0#累计误差
        self.last_last_err=0
    def cmd_pid(self):
        """位置式PID控制"""
        self.last_err=self.now_err
        self.now_err=self.exp_val-self.now_val
        self.sum_err+=self.now_err

        self.now_val=self.kp*self.now_err+self.ki*self.sum_err+self.kd*(self.now_err-self.last_err)
        return self.now_val
    def pid_cmd(self):
        """增量式PID控制"""
        self.last_last_err=self.last_err
        self.last_err=self.now_err
        self.now_err=self.exp_val-self.now_val
        self.now_err-=50*random.random()
        self.change_val=self.kp*(self.now_err-self.last_err)+self.ki*self.now_err+self.kd*(self.now_err-2*self.last_err+self.last_last_err)
        self.now_val+=self.change_val
        return self.now_val
        
pid1=[5,]
plt.ion()
my_pid=pid(1000,0.1,0.15,0.01)
for i in range(100):
    # my_pid.exp_val=15
    pid1.append(my_pid.pid_cmd())
    # my_pid.exp_val=12
    # pid1.append(my_pid.pid_cmd())
    
    plt.plot(pid1,'-r')
    plt.pause(0.01)

plt.ioff()
plt.show()