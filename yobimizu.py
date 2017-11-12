def los(dis):
    print('los->', dis)
def rot(dis):
    print('rot->', dis)
def mov(policy, dis):
    if policy =='los':
        los(dis)
    if policy =='rot':
        rot(dis)


class Planner(object):
    def __init__(self):
        self.trace = []
    
    def _move(self, policy, dis):
        if policy =='los':
            los(dis)
        if policy =='rot':
            rot(dis)
    
    def move(self, policy, dis):
        self._move(policy, dis)
        mov = policy, dis
        self.trace.append(mov)
    
    def reverse(self):
        for mov in self.trace[::-1]:
            policy, dis = mov
            self._move(policy, -dis)
    
    def ending(self):
        import math
        l2 = lambda x, y: math.sqrt(x**+y**2)

        info = client.GetLastMsg[RobotInfo]()
        x, y, theta = info.posx, info.posy, info.heading
        self._move('rot', -theta)
        self._move('los', -l2(x,y))
        


plan = Planner()
plan.move('los',0.2)
plan.move('rot', -5)
plan.move('los',0.2)
plan.move('rot', 2)
plan.reverse()


def plan_stop():
    order =  SpeechOrder()
    order.utterace = ToBytes("�Ă��������")
    client.Send( order )
    
    order = RobotOrder()
    order.kind = RobotOrder.ORDER_STOP;
    client.Send( order )


def red_stop():
    '''�F���o���ʂ���M'''
    color = client.GetLastMsg[ColorBlobs]()
    if color:
        for i in range( color.data.Count ):
            print "�F���o�@id:" , color.data[i].id, " pos:",color.data[i].pos.x, color.data[i].pos.y, color.data[i].pos.z

        plan_stop()


def isClision()
    info = client.GetLastMsg[RobotInfo]()
    if not info:
        return
    print "�Փ�(���C���S�C�E):" , info.isClisionDetectedL , info.isClisionDetectedC , info.isClisionDetectedR
    return info.isClisionDetectedL or info.isClisionDetectedC or info.isClisionDetectedR    



def isFound()
    skeltons = client.GetLastMsg[Skeltons]()
    if not skeltons:
        return

    if not skeltons.data.Count:
        return
    rightUp = False
    leftUp = False
    rightFront = False
    leftFront = False
    rightSide = False
    leftSide = False

    # ��̍��W�Ɠ��̍��W����Ɏ�̏�Ԃ�����
    if skeltons.data[0].joints[Skelton.SKEL_RIGHT_HAND].y - skeltons.data[0].joints[Skelton.SKEL_HEAD].y > 0: rightUp = True;
    if skeltons.data[0].joints[Skelton.SKEL_LEFT_HAND].y - skeltons.data[0].joints[Skelton.SKEL_HEAD].y > 0: leftUp = True;

    if skeltons.data[0].joints[Skelton.SKEL_HEAD].z - skeltons.data[0].joints[Skelton.SKEL_RIGHT_HAND].z > 300: rightFront = True;
    if skeltons.data[0].joints[Skelton.SKEL_HEAD].z - skeltons.data[0].joints[Skelton.SKEL_LEFT_HAND].z > 300: leftFront = True;

    if skeltons.data[0].joints[Skelton.SKEL_RIGHT_HAND].x - skeltons.data[0].joints[Skelton.SKEL_RIGHT_SHOULDER].x < -300: rightSide = True;
    if skeltons.data[0].joints[Skelton.SKEL_LEFT_HAND].x - skeltons.data[0].joints[Skelton.SKEL_LEFT_SHOULDER].x > 300: leftSide = True;

    print "�E��F",
    if rightUp:       print "��",
    if rightFront:    print "�O",
    if rightSide:     print "��",
    print

    print "����F",
    if leftUp:      print "��",
    if leftFront:   print "�O",
    if leftSide:    print "��",
    print
    
    return rightUp or leftUp or rightFront or leftFront or rightSide or leftSide


def track():        
    while( not isClision() ):
        if not isFound():
            plan.move('rot',1)
            continue
        
        plan.move('los',10)
        los(10)













