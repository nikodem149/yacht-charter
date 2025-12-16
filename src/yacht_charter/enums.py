from enum import StrEnum


class SailBoatStatus(StrEnum):
    AVAILABLE = "available"  # boat ready for charter
    BOOKED = "booked"  # reserved and waiting
    IN_USE = "in_use"  # currently in charter
    MAINTENANCE = "maintenance"  # in repair
    INACTIVE = "inactive" # not active and not to display
    DECOMMISSIONED = "decommissioned"  # no longer in use

ALLOWED_STATUS_TRANSITIONS = {
    SailBoatStatus.AVAILABLE: [
        SailBoatStatus.BOOKED,
        SailBoatStatus.MAINTENANCE,
        SailBoatStatus.INACTIVE
    ],
    SailBoatStatus.BOOKED: [
        SailBoatStatus.AVAILABLE, # if reservation cancelled, boat is available again
        SailBoatStatus.IN_USE
    ],
    SailBoatStatus.IN_USE: [
        SailBoatStatus.AVAILABLE,
        SailBoatStatus.MAINTENANCE,
    ],
    SailBoatStatus.MAINTENANCE: [
        SailBoatStatus.AVAILABLE,
        SailBoatStatus.INACTIVE
    ],
    SailBoatStatus.INACTIVE: [
        SailBoatStatus.AVAILABLE,
        SailBoatStatus.DECOMMISSIONED
    ],
    SailBoatStatus.DECOMMISSIONED: []
}

# moduł helper z jedną funkcją
def can_change_status(current, new) -> bool:
    return new in ALLOWED_STATUS_TRANSITIONS.get(current, [])
