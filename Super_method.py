class Camera:
    cam = 'Shoot'

    def foto(self):
        print(self.cam)





class Phone:
    phone = 'Calling'

    def calling(self):
        print(self.phone)

    def typing(self):
        return 'typing !'


class CameraPhone(Camera, Phone):
    def __init__(self):
        super().__init__()


mobile1 = CameraPhone()
mobile1.foto()
mobile1.calling()
typing()
