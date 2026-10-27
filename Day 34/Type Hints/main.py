# age: int
# name: str
# height: float
# is_human: bool
#
# age = "twelve"

def police_check(age: int) -> bool: # accepts input int, returns boolean
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

police_check("twelve")