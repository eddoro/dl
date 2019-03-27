import adv_test
import adv

def module():
    return H_Edward

class H_Edward(adv.Adv):
    def pre(this):
        if this.condition('hp100'):
            this.conf['mod_a'] = ('att' , 'passive', 0.1)


if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1
        `s2, seq=5 
        `s3
        """
    adv_test.test(module(), conf, verbose=0)

