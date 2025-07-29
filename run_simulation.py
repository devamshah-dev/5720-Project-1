# simulations/run_simulation.py
import sys
import os

# Python find custom package & add the engine/ directory to the system path.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.engine import TrustEngine
from engine.user_profiles import user_profile, create_safe_scenario, create_suspicious_scenario, create_anomaly_scenario
from engine.config import CRITICAL_RISK_THRESHOLD, MODERATE_RISK_THRESHOLD

# single scenario
def run_scenario(scenario_name, context, engine):
    print(f"\n--- [SCENARIO: {scenario_name}] ---")
    score, reasons = engine.assess_context(context)
    print(f"  > Calculated Trust Score: {score}%")
    if reasons:
        print(f"  > Reasons for score change: {', '.join(reasons)}")
    if score < CRITICAL_RISK_THRESHOLD:
        print("  > System Action: CRITICAL RISK. Lock device immediately.")
    elif score < MODERATE_RISK_THRESHOLD:
        print("  > System Action: MODERATE RISK. Require step-up authentication.")
    else:
        print("  > System Action: HIGH TRUST. Seamless access granted.")
    print("--------------------------------------")

# main function - all scenarios
def main():
    print("Initializing AURA Engine...")
    # Create an instance of the engine with the user's profile
    engine = TrustEngine(user_profile)
    run_scenario("Legitimate user at home", create_safe_scenario(), engine)
    run_scenario("Suspicious user in unknown location", create_suspicious_scenario(), engine)
    run_scenario("Illegitimate user with typing anomaly", create_anomaly_scenario(), engine)

if __name__ == "__main__":
    main()