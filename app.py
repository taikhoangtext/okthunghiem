from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="sample", rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},)