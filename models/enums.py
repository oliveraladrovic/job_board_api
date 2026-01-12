from enum import Enum

class UserRole(str, Enum):
    admin = "admin"
    employer = "employer"
    candidate = "candidate"

class ApplicationStatus(str, Enum):
    applied = "applied"
    rejected = "rejected"
    accepted = "accepted"