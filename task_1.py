from time import sleep


class TrafficLight:
    traffic_color_time = {"Red": 7, "Yellow": 2, "Green": 5}
    traffic_color_order = {"Red": set(["Yellow"]), "Yellow": set(["Red", "Green"]), "Green": set(["Yellow"])}

    def __init__(self):
        self.__color = "Red"

    def running(self, color_list):
        last_color = None
        for self.__color in color_list:
            tm = TrafficLight.traffic_color_time.get(self.__color)
            if not tm:
                print(f"Такого цвета нет: {self.__color}")
                return
            if last_color:
                if not (self.__color in TrafficLight.traffic_color_order[last_color]):
                    print(f"Неверная последовательность цветов: {last_color} -> {self.__color}")
                    return
            last_color = self.__color
            print(self.__color)
            sleep(tm)
        print("Stop")


my_traffic_light = TrafficLight()
my_traffic_light.running(["Red", "Yellow", "Green", "Yellow"])
