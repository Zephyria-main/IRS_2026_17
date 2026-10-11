import json

import rclpy
from std_msgs.msg import String


def main():
    rclpy.init()
    node = rclpy.create_node('plc_hmi_listener')

    def listener_callback(msg):
        try:
            data = json.loads(msg.data)  # parse JSON string into Python dict
            stamp = data["stamp"]
            box = data["box"]
            counts = data["counts"]

            print("Received PLC status:")
            print(f"Time: {stamp['sec']}.{stamp['nanosec']}")
            print(f"Box weight raw={box['weight_raw']}")
            print(f"Location: {box['location']}")
            print(f"Counts: big={counts['big']}, medium={counts['medium']}, "
                  f"small={counts['small']}, total={counts['total']}")
            print()
        except Exception as e:
            node.get_logger().error(f"Failed to parse JSON: {e}\nRaw msg={msg.data}")

    node.create_subscription(String, '/hmi/unified_status', listener_callback, 10)
    rclpy.spin(node)


if __name__ == '__main__':
    main()