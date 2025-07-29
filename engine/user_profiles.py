# engine/profiles.py

user_profile = {
    # Biometrics
    "face_id": "user_dev_u0_260",
    "pin_timing_pattern_ms": [120, 95, 110],  # 1-3-5-7
    
    # Environmental Context
    "home_location": (43.9632, 78.9571),  # Brooklin
    "university_location": (43.9456, 78.8968), # Ontario Tech (North Campus)
    "known_wifi": ["CAMPUS-AIR", "eduroam", "Little_Brooklin"],
    
    # behavioral Context
    "typical_motion_states": ["sitting_still", "walking_calmly"]
}

def create_safe_scenario():
    #legitimate user at home.
    return {
        "detected_face_id": user_profile["face_id"],
        "nearby_wifi_list": ["Little_Brooklin", "BELL520", "Dave-2"],
        # currently distance limit is within 500 meters of Home or University location!
        "current_gps": (user_profile["home_location"][0] + 0.0001, user_profile["home_location"][1] - 0.0001),
        "current_motion_state": "sitting_still"
    }

def create_suspicious_scenario():
    # unknown user in unsafe location.
    return {
        "detected_face_id": "unknow_face_u129", # A different face
        "nearby_wifi_list": ["Tim_Hortons_Ajax14", "Brooklin_South_Park"], # Unknown networks
        "current_gps": (43.9045, 78.8589), # Dylan's No frills Oshawa
        "current_motion_state": "unstable_shaking" # Atypical
    }

def create_anomaly_scenario():
    # real user typing PIN hastely
    return {
        "nearby_wifi_list": ["CAMPING-AIR", "eduroam"], # known Wi-Fi
        "current_gps": user_profile["university_location"], # location is known
        "last_pin_timing_ms": [250, 100, 280], # Erratic typing
        "current_motion_state": "sitting_still"
    }