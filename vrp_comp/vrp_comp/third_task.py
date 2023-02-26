import rclpy
from vrp_comp.do_task import DoTask

class DoThirdTask(DoTask):
    def __init__(self):
        super().__init__('third_task')
        self.start()

    def task(self, latitude, longitude, cog, hdg, speed, img):
        """
        :param latitude: географическая широта в градусах от -90 до 90; Float
        :param longitude: географическая долгота в градусах от -180 до 180; Float
        :param cog: Направление скорости относительно севера в градусах от -180 до 180; Float
        :param hdg: Направление носа относительно севера в градусах от -180 до 180; Float
        :param speed: Скорость в метрах в секунду; Float
        :return: Мощность на каждом двигателе {'mode': 1, 'l': (-1,1), 'r': (-1,1), 'b': (-1,1)}
            или направление {'mode': 0, 'x': (-1,1), 'y': (-1,1), 'z': (-1,1)}
        """

        # РАСПОЛОЖИТЕ ВАШ КОД ДАЛЕЕ
        
        return {'mode': 1, 'l': 0, 'r': 0, 'b': 0}


def main(args=None):
    rclpy.init(args=args)
    task = DoThirdTask()
    rclpy.spin(task)
    rclpy.shutdown()


if __name__ == '__main__':
    main()