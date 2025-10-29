from pythonosc.udp_client import SimpleUDPClient

def set_main_vol(ip, port, volume):
	client = SimpleUDPClient(ip, port)
	client.send_message("/main/st/mix/fader", [volume])

def load_scene(ip, port, scene_id):
	client = SimpleUDPClient(ip, port)
	client.send_message("/load", ["scene", scene_id])
