import rclpy
from std_msgs.msg import String


def main():
    print('Hi from pa_warehouse_status.')

    rclpy.init()
    node = rclpy.create_node('pineapple_gossip_bot')
    publisher = node.create_publisher(String, 'status_updates', 10)

    def publish_status():
        msg = String()
        msg.data = 'My partner just lost a sibling, I dont have time to be creative.'
        publisher.publish(msg)
        print('Published:', msg.data)

    node.create_timer(2.0, publish_status)
    rclpy.spin(node)


if __name__ == '__main__':
    main()
