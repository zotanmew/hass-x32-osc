from pythonosc.udp_client import SimpleUDPClient

def x32_set_main_vol(ip, port, volume):
	client = SimpleUDPClient(ip, port)
	client.send_message("/main/st/mix/fader", [volume])

def x32_load_scene(ip, port, scene_id):
	client = SimpleUDPClient(ip, port)
	client.send_message("/load", ["scene", scene_id])
