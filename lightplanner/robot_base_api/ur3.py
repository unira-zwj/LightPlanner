from urx import URRobot


class UR3():
    def __init__(self, ip="192.168.0.1") -> None:
        self.rob = URRobot(ip)
    
    def get_pos(self):
        print(self.rob.getl())
    
    def movel(self, pos, acc=0.5, vel=0.3, wait=True):
        print(pos)
        self.rob.movel(pos, acc=acc, vel=vel, wait=wait)
    
    
    
if __name__ == '__main__':
    gripper = UR3()
    gripper.get_pos()
    # gripper.movel(pos)