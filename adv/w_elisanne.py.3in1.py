import adv_test
from adv import *
from slot.a import *

def module():
    return W_Elisanne


class W_Elisanne(Adv):
    comment = 'c2+fs; 2in1'
    
    conf = {}
    def d_slots(this):
        if 'bow' in this.ex:
            this.conf.slot.a = TSO()+FRH()
        else:
            this.conf.slot.a = TSO()+JotS()

    a1 = ('sp',0.08)
    a3 = ('bc',0.13)

    def prerun(this):
        this.s2debuff = Debuff('s2defdown',0.15,10.5,1)
        if this.condition('s2 defdown for 10s'):
            this.s2defdown = 1
        else:
            this.s2defdown = 1

    def s2_proc(this, e):
        if this.s2defdown :
            this.s2debuff.on()

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1,this.s2debuff.get()
        `s1,fsc and s2.charged<s2.sp-749
        `s2
        `s3,fsc
        `fs,seq=2 and cancel and s1.charged>=909 and not this.s2debuff.get()
        `fs,seq=3 and cancel
    """

    adv_test.test(module(), conf, verbose=0, mass=0)
    adv_test.sum_ac()
