#engine/config.py

# penalty - biometric(high-2), physical(med-2),behavioural(med-1)
FACE_ID_MISMATCH_PENALTY = -70
PIN_RHYTHM_MISMATCH_PENALTY = -40
NO_KNOWN_WIFI_PENALTY = -20
UNKNOWN_LOCATION_PENALTY = -15
UNUSUAL_MOTION_STATE_PENALTY = -25

# trust-score - base
CRITICAL_RISK_THRESHOLD = 40  # locks the device below 40
MODERATE_RISK_THRESHOLD = 85  # require step-up auth below 85

# global-maxima of safe-zone location distance(abstract,no units), before unknown
LOCATION_TOLERANCE_RADIUS = 0.1

# maximum possible difference in PIN timing patterns before flagged.
MAX_PIN_TIMING_DIFFERENCE = 100  # PIN deviation in ms
MAX_SAFE_ZONE_DISTANCE = 0.1