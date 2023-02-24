from enum import Enum


EVENT_TYPE_TO_NAME = {
    "1": "Soccer",
    "2": "Tennis",
    "3": "Golf",
    "4": "Cricket",
    "5": "Rugby Union",
    "1477": "Rugby League",
    "6": "Boxing",
    "7": "Horse Racing",
    "8": "Motor Sport",
    "27454571": "Esports",
    "10": "Special Bets",
    "998917": "Volleyball",
    "11": "Cycling",
    "2152880": "Gaelic Games",
    "3988": "Athletics",
    "6422": "Snooker",
    "7511": "Baseball",
    "6231": "Financial Bets",
    "6423": "American Football",
    "7522": "Basketball",
    "7524": "Ice Hockey",
    "61420": "Australian Rules",
    "468328": "Handball",
    "3503": "Darts",
    "26420387": "Mixed Martial Arts",
    "4339": "Greyhound Racing",
    "2378961": "Politics",
}


class OrderType(Enum):
    LIMIT = "LIMIT"
    MARKET_ON_CLOSE = "MARKET_ON_CLOSE"


class OrderSide(Enum):
    BACK = "BACK"
    LAY = "LAY"


class OrderResponse(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class OrderStatus(Enum):
    EXECUTABLE = "EXECUTABLE"
    EXECUTION_COMPLETE = "EXECUTION_COMPLETE"
