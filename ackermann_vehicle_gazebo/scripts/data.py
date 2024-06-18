#!/usr/bin/env python3
import rospy
import csv
from nav_msgs.msg import Odometry

# Initialize ROS node
rospy.init_node('position_logger_separate', anonymous=True)

# File paths
leader_file_path = 'leader_positions.csv'
follower1_file_path = 'follower1_positions.csv'
follower2_file_path = 'follower2_positions.csv'

# Setup CSV files
def setup_csv_writer(file_path):
    file = open(file_path, mode='w', newline='')  # 'w' mode overwrites the file
    writer = csv.DictWriter(file, fieldnames=['timestamp', 'x', 'y'])
    writer.writeheader()
    return file, writer


leader_file, leader_writer = setup_csv_writer(leader_file_path)
follower1_file, follower1_writer = setup_csv_writer(follower1_file_path)
follower2_file, follower2_writer = setup_csv_writer(follower2_file_path)

def callback(data, args):
    """ Callback function to handle odometry messages. """
    entity, writer = args
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    timestamp = rospy.Time.now().to_sec()
    # Write data to corresponding CSV file
    writer.writerow({'timestamp': timestamp, 'x': x, 'y': y})

# Subscribers for leader and followers
rospy.Subscriber("/odom", Odometry, callback, callback_args=('leader', leader_writer))
rospy.Subscriber("/robot1/odom", Odometry, callback, callback_args=('follower1', follower1_writer))
rospy.Subscriber("/robot2/odom", Odometry, callback, callback_args=('follower2', follower2_writer))

# ROS spin to keep the node running
rospy.spin()

# Close files properly on shutdown
def close_files():
    leader_file.close()
    follower1_file.close()
    follower2_file.close()

rospy.on_shutdown(close_files)
