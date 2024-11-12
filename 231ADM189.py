# Function to decide the commute based on conditions
def commute_decision(rain, heavy_traffic, early_meeting, strike, appointment, road_construction):
    # Work from Home (WFH) is preferred if it's raining or you have an early meeting
    WFH = rain or early_meeting

    # Drive is preferred if it's not raining, traffic is light, and there's no road construction
    Drive = (not rain and not heavy_traffic and not road_construction) or appointment

    # Public Transport is preferred if there's no strike, it's not raining, and traffic is heavy
    PublicTransport = not strike and not rain and heavy_traffic

    return WFH, Drive, PublicTransport


# Example scenarios
scenarios = [
    {"rain": True, "heavy_traffic": True, "early_meeting": False, "strike": False, "appointment": False,
     "road_construction": False},  # Scenario 1
    {"rain": False, "heavy_traffic": False, "early_meeting": False, "strike": True, "appointment": False,
     "road_construction": False},  # Scenario 2
    {"rain": False, "heavy_traffic": False, "early_meeting": False, "strike": False, "appointment": False,
     "road_construction": False},  # Scenario 3
]

# Checking the assistant's decision for each scenario
for idx, scenario in enumerate(scenarios):
    WFH, Drive, PublicTransport = commute_decision(**scenario)
    print(f"Scenario {idx + 1}:")
    print(f"  Work from Home: {WFH}")
    print(f"  Drive: {Drive}")
    print(f"  Public Transport: {PublicTransport}")
    print()


# Function to simulate specific queries
def query_commute(option, rain, heavy_traffic, early_meeting, strike, appointment, road_construction):
    WFH, Drive, PublicTransport = commute_decision(rain, heavy_traffic, early_meeting, strike, appointment,
                                                   road_construction)

    if option == "WFH":
        return WFH
    elif option == "Drive":
        return Drive
    elif option == "PublicTransport":
        return PublicTransport
    else:
        return None


# Sample queries for different commuting options
print("Query Results:")
print(
    f"Should you work from home? {query_commute('WFH', rain=True, heavy_traffic=False, early_meeting=True, strike=False, appointment=False, road_construction=False)}")
print(
    f"Should you drive? {query_commute('Drive', rain=False, heavy_traffic=False, early_meeting=False, strike=False, appointment=False, road_construction=False)}")
print(
    f"Should you take public transport? {query_commute('PublicTransport', rain=False, heavy_traffic=True, early_meeting=False, strike=False, appointment=False, road_construction=False)}")


# Extended rules for specific conditions

# Function to check for route options based on road construction and traffic
def driving_route(rain, heavy_traffic, road_construction):
    if road_construction and not heavy_traffic:
        return "Take Route 1 (Construction, but light traffic)"
    elif heavy_traffic and not road_construction:
        return "Take Route 2 (Heavy traffic, no construction)"
    elif not heavy_traffic and not road_construction:
        return "Take Route 3 (Clear road)"
    else:
        return "No optimal route available"


# Extended scenarios including road conditions
extended_scenarios = [
    {"rain": False, "heavy_traffic": True, "early_meeting": False, "strike": False, "appointment": False,
     "road_construction": True},  # Road construction with heavy traffic
    {"rain": False, "heavy_traffic": False, "early_meeting": False, "strike": False, "appointment": False,
     "road_construction": False},  # Clear conditions
]

# Checking for the driving route based on the extended scenarios
for idx, scenario in enumerate(extended_scenarios):
    route = driving_route(scenario["rain"], scenario["heavy_traffic"], scenario["road_construction"])
    print(f"Scenario {idx + 1} Driving Route: {route}")
