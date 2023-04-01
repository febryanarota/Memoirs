from AuthHandler.Entity.Passcode import *

class AuthController():
    def login(self, inputPasscode):
        # Return 0 if success, 1 if not valid, and 2 if failed
        if(len(inputPasscode) != 6):
            return 1
        else:
            # Create entity
            entityPasscode = Passcode()
            
            # Get passcode
            passcode = entityPasscode.getPasscode()
            if(inputPasscode != passcode):
                return 2
            else:
                return 0
    
    def register(self, inputPasscode):
        # Return 0 if success and 1 if not valid
        if(len(inputPasscode) != 6):
            return 1
        else:
            # Create entity
            entityPasscode = Passcode(inputPasscode)

            # Set passcode
            entityPasscode.setPasscode()
            return 0
