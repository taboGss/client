import argparse
import cv2
import client

from rtsp.auxiliar_functions import Screen
from rtsp.connection import cam_rtsp


def main():
    
    client.connect_to_launcher() # Conectarse al EndPoint 
    rtsp, distance, poly, orientation, zone_id, = \
    									client.get_parameters(client.SPEED)
    
    template = client.get_endpoint_template(client.SPEED)

    template['device_id'] = 14
    template['zone_id'] = zone_id
    template['license_plate'] = "UZW123"
    template['avg_speed'] = "333"
    template['max_speed'] = "333"
    template['video_url'] = "None"

	# Subir nuevo registro
    status = client.post_update(template, client.SPEED)
    client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--rtsp', type=str, default="", help='position')
    parser.add_argument('--id', type=str, default="", help='position2')
    opt = parser.parse_args()

    main()
