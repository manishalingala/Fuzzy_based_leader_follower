#!/bin/bash
# Run ROS Python scripts in the background with a 2-second interval between each

# Start the leader script
python3 new_leader.py &
sleep 2

# Start the follower2 script
python3 Follower2.py &
sleep 2

# Start the follower1 script
python3 Follower1.py &
sleep 2

# Start the data logging script
python3 data.py &
wait

