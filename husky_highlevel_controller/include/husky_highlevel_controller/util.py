from sensor_msgs.msg import LaserScan

def filter_scan(data):
    ranges_filtered = (v for v in data.ranges if v > data.range_min)
    min_distance = min(ranges_filtered)
    min_index = data.ranges.index(min_distance)
    start_index = min_index - 2
    no_distances = 5

    measurements_5 = data.ranges[start_index : (start_index + no_distances)]

    new_msg = LaserScan()
    new_msg = data
    new_msg.angle_min = data.angle_min + (start_index * data.angle_increment)
    new_msg.angle_max = new_msg.angle_min + (no_distances-1) * data.angle_increment
    new_msg.ranges = measurements_5

    return new_msg