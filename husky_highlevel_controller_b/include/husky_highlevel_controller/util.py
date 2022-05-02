from sensor_msgs.msg import LaserScan

def filter_scan(data):
    min_distance = data.range_min
    # filter ranges and discard all distances < min_distance
    ranges_filtered = (v for v in data.ranges if v > min_distance)

    # get min distance in ranges since the recieved min_distance seems to not appear in the ranges list (?)
    min_range = min(ranges_filtered)
    min_index = data.ranges.index(min_range)

    # get 2 values left and right from the min distance
    min_distance_neighbourhood = data.ranges[min_index-2: min_index+3]

    # Calculate the new min and max angle (now of the 5 "min distance neighbourhood" values)
    new_angle_min = data.angle_min + (min_index-2) * data.angle_increment
    new_angle_max = new_angle_min + 4 * data.angle_increment

    # create the new LaserScan message
    filtered_msg = LaserScan()
    filtered_msg = data
    filtered_msg.angle_min = new_angle_min
    filtered_msg.angle_max = new_angle_max
    filtered_msg.ranges = min_distance_neighbourhood

    return filtered_msg
