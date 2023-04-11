# useful constants during analysis

FEATURES = [
    'CIRCLE', 'SQUARE', 'STAR', 'TRIANGLE', 
    'CYAN', 'GREEN', 'MAGENTA', 'YELLOW', 
    'ESCHER', 'POLKADOT', 'RIPPLE', 'SWIRL'
]

COLUMN_NAMES = FEATURES + ["CORRECT", "INCORRECT"]

# time in miliseconds for required fixation on a card to register a choice
# also time between choice and feedback signals
CHOICE_FIXATION_TIME = 800