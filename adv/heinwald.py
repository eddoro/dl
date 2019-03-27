import adv_test
from adv import *

def module():
    return Heinwald

class Heinwald(Adv):

    def pre(this):
        if this.condition("hp70"):
            this.conf['mod_a'] = ('s','passive',0.35)
        if this.condition("buff all teammates"):
            this.s2_proc = this.c_s2_proc


    def init(this):
        this.charge_p('prep','100%')
        this.s2ssbuff = Selfbuff("s2_shapshifts1",1, 10,'ss','ss')


    def c_s2_proc(this, e):
        this.s2ssbuff.on()
        Teambuff('s2team',0.1,10).on()
        Selfbuff('s2self',0.1,10).on()

    def s2_proc(this, e):
        this.s2ssbuff.on()
        Selfbuff('s2',0.2,10).on()


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5
        `s2, seq=5
        `s3, seq=5
        """
    adv_test.test(module(), conf,verbose=0, mass=0)

