# useful constants during analysis

FEATURES = [
    'CIRCLE', 'SQUARE', 'STAR', 'TRIANGLE', 
    'CYAN', 'GREEN', 'MAGENTA', 'YELLOW', 
    'ESCHER', 'POLKADOT', 'RIPPLE', 'SWIRL'
]

NUM_UNITS = 59

COLUMN_NAMES_W_UNITS = FEATURES + ["CORRECT", "INCORRECT"] + [f"unit_{i}" for i in range(0, NUM_UNITS)]
COLUMN_NAMES = FEATURES + ["CORRECT", "INCORRECT"]