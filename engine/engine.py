# engine/engine.py
import math
import importlib
config = importlib.import_module('engine.config')

class TrustEngine:
    def __init__(self, user_profile):
        self.profile = user_profile
        self.score = 100
        self.reasons = []

    def assess_context(self, current_context):
        # trust score upon context
        self.score = 100  # Reset score per unlock-session
        self.reasons = []

        self._check_face(current_context)
        self._check_pin_rhythm(current_context)
        self._check_wifi(current_context)
        self._check_location(current_context)
        self._check_motion(current_context)
        
        self.score = max(0, self.score)
        return self.score, self.reasons

    def _check_face(self, context):
        if "detected_face_id" in context and self.profile["face_id"] != context["detected_face_id"]:
            self.score += config.FACE_ID_MISMATCH_PENALTY
            self.reasons.append("Face ID mismatch")

    def _check_pin_rhythm(self, context):
        if "last_pin_timing_ms" in context:
            timing_diff = sum(abs(p - c) for p, c in zip(self.profile["pin_timing_pattern_ms"], context["last_pin_timing_ms"]))
            if timing_diff > config.MAX_PIN_TIMING_DIFFERENCE:
                self.score += config.PIN_RHYTHM_MISMATCH_PENALTY
                self.reasons.append("PIN typing fraud!")

    def _check_wifi(self, context):
        known_found = set(self.profile["known_wifi"]) & set(context.get("nearby_wifi_list", []))
        if not known_found:
            self.score += config.NO_KNOWN_WIFI_PENALTY
            self.reasons.append("No known Wi-Fi networks nearby")

    def _check_location(self, context):
        current_gps = context.get("current_gps")
        if current_gps:
            dist_home = math.dist(self.profile["home_location"], current_gps)
            dist_office = math.dist(self.profile["university_location"], current_gps)
            if dist_home > config.MAX_SAFE_ZONE_DISTANCE and dist_office > config.MAX_SAFE_ZONE_DISTANCE:
                self.score += config.UNKNOWN_LOCATION_PENALTY
                self.reasons.append("Location is far from safe zones")

    def _check_motion(self, context):
        motion = context.get("current_motion_state")
        if motion and motion not in self.profile["typical_motion_states"]:
            self.score += config.UNUSUAL_MOTION_STATE_PENALTY
            self.reasons.append(f"Unusual motion: {motion}")