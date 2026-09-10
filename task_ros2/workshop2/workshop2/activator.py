import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool


class Activator(Node):
    def __init__(self):
        super().__init__('activator')
        self.get_logger().info("Service Client Node Started!!")
        self.send_request()

    def send_request(self):
        self.client = self.create_client(SetBool, 'activate')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, waiting again...")

        self.request = SetBool.Request()
        self.request.data = True
        future = self.client.call_async(self.request)
        future.add_done_callback(self.service_callback)

    def service_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f"Service response: {response.success}")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")



def main(args=None):
    rclpy.init(args=args)
    node = Activator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()