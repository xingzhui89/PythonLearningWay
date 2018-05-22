'''

'''
class BlackMedium:
    feture='Ugly'
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr

    def sell_house(self):
        print('[%s] 正在卖房子，傻逼才买呢' % self.name)
    def rent_house(self):
        print(print('[%s] 正在租房子，傻逼才买呢' % self.name))

print(hasattr(BlackMedium,'feature'))

b1=BlackMedium('万成置地', '天露园')
print(b1.__dict__)
print(hasattr(b1,'name'))
print(getattr(b1, 'feture'))
func=getattr(b1,'rent_house')
func()

setattr(b1,'sb',True)

print(b1.__dict__)

delattr(b1,'sb')

print(b1.__dict__)
