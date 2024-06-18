import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the data from CSV files
leader_data = pd.read_csv('/home/navaneet/Desktop/vehicle_ws/src/ackermann_vehicle/ackermann_vehicle_gazebo/scripts/leader_positions.csv')
follower1_data = pd.read_csv('/home/navaneet/Desktop/vehicle_ws/src/ackermann_vehicle/ackermann_vehicle_gazebo/scripts/follower1_positions.csv')
follower2_data = pd.read_csv('/home/navaneet/Desktop/vehicle_ws/src/ackermann_vehicle/ackermann_vehicle_gazebo/scripts/follower2_positions.csv')  # Assuming this is correct, adjust if necessary

# Define a constant z-value
z_constant = 0.5

# Create a larger 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot each dataset with a constant z-value
ax.scatter(leader_data['x'], leader_data['y'], z_constant, label='Leader', color='r', marker='o', s=50)
ax.scatter(follower1_data['x'], follower1_data['y'], z_constant, label='Follower 1', color='g', marker='^', s=50)
ax.scatter(follower2_data['x'], follower2_data['y'], z_constant, label='Follower 2', color='b', marker='s', s=50)

# Labels and Title
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_zlabel('Z Position')
ax.set_title('3D Position Tracking of Robots')

# Grid and limits
ax.grid(True)
ax.set_xlim(min(leader_data['x'].min(), follower1_data['x'].min(), follower2_data['x'].min()), 
            max(leader_data['x'].max(), follower1_data['x'].max(), follower2_data['x'].max()))
ax.set_ylim(min(leader_data['y'].min(), follower1_data['y'].min(), follower2_data['y'].min()), 
            max(leader_data['y'].max(), follower1_data['y'].max(), follower2_data['y'].max()))
ax.set_zlim(0, 1)  # Since z is constant, this can be set from 0 to 1 for better visualization

# Legend with increased font size
ax.legend(fontsize=30)

# Show plot
plt.show()
