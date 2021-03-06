from codeinternals.ctre import BaseTalon


class TalonSRX(BaseTalon):
    """ CTRE Talon SRX Motor Controller when used on CAN Bus. """

    def configAllSettings(self, allConfigs, timeoutMs=50):  # real signature unknown; restored from __doc__
        """
        configAllSettings(self: ctre._ctre.TalonSRX, allConfigs: ctre._ctre.TalonSRXConfiguration, timeoutMs: int = 50) -> ctre._ctre.ErrorCode
        
        Configures all persistent settings.
        
        :param allConfigs: Object with all of the persistant settings
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                  config success and report an error if it times out.
                  If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configContinuousCurrentLimit(self, amps, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        configContinuousCurrentLimit(self: ctre._ctre.TalonSRX, amps: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Configure the continuous allowable current-draw (when current limit is
        enabled).
        
        Supply current limiting is also available via ConfigSupplyCurrentLimit(),
        which is a common routine with Talon FX.
        
        Current limit is activated when current exceeds the peak limit for longer
        than the peak duration. Then software will limit to the continuous limit.
        This ensures current limiting while allowing for momentary excess current
        events.
        
        For simpler current-limiting (single threshold) use
        ConfigContinuousCurrentLimit() and set the peak to zero:
        ConfigPeakCurrentLimit(0).
        
        :param amps: Amperes to limit.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for config
                 success and report an error if it times out. If zero, no
                 blocking or checking is performed.
        """
        pass

    def configPeakCurrentDuration(self, milliseconds, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        configPeakCurrentDuration(self: ctre._ctre.TalonSRX, milliseconds: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Configure the peak allowable duration (when current limit is enabled).
        
        Supply current limiting is also available via ConfigSupplyCurrentLimit(),
        which is a common routine with Talon FX.
        
        Current limit is activated when current exceeds the peak limit for longer
        than the peak duration. Then software will limit to the continuous limit.
        This ensures current limiting while allowing for momentary excess current
        events.
        
        For simpler current-limiting (single threshold) use
        ConfigContinuousCurrentLimit() and set the peak to zero:
        ConfigPeakCurrentLimit(0).
        
        :param milliseconds: How long to allow current-draw past peak limit.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for config
                    success and report an error if it times out. If zero, no
                    blocking or checking is performed.
        """
        pass

    def configPeakCurrentLimit(self, amps, timeoutMs=0):  # real signature unknown; restored from __doc__
        """
        configPeakCurrentLimit(self: ctre._ctre.TalonSRX, amps: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Configure the peak allowable current (when current limit is enabled).
        
        Supply current limiting is also available via ConfigSupplyCurrentLimit(),
        which is a common routine with Talon FX.
        
        Current limit is activated when current exceeds the peak limit for longer
        than the peak duration. Then software will limit to the continuous limit.
        This ensures current limiting while allowing for momentary excess current
        events.
        
        For simpler current-limiting (single threshold) use
        ConfigContinuousCurrentLimit() and set the peak to zero:
        ConfigPeakCurrentLimit(0).
        
        :param amps: Amperes to limit.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for config
                 success and report an error if it times out. If zero, no
                 blocking or checking is performed.
        """
        pass

    def configSelectedFeedbackSensor(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        configSelectedFeedbackSensor(*args, **kwargs)
        Overloaded function.
        
        1. configSelectedFeedbackSensor(self: ctre._ctre.TalonSRX, feedbackDevice: ctre._ctre.TalonSRXFeedbackDevice, pidIdx: int = 0, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Select the feedback device for the motor controller.
        
        :param feedbackDevice: Talon SRX Feedback Device to select.
        
        :param pidIdx: 0 for Primary closed-loop. 1 for auxiliary closed-loop.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                      config success and report an error if it times out.
                      If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        
        2. configSelectedFeedbackSensor(self: ctre._ctre.TalonSRX, feedbackDevice: ctre._ctre.FeedbackDevice, pidIdx: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode
        
        Select the feedback device for the motor controller.
        
        :param feedbackDevice: Feedback Device to select.
        
        :param pidIdx: 0 for Primary closed-loop. 1 for auxiliary closed-loop.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                      config success and report an error if it times out.
                      If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        
        3. configSelectedFeedbackSensor(self: ctre._ctre.TalonSRX, feedbackDevice: ctre._ctre.RemoteFeedbackDevice, pidIdx: int, timeoutMs: int) -> ctre._ctre.ErrorCode
        
        Select the remote feedback device for the motor controller.
        Most CTRE CAN motor controllers will support remote sensors over CAN.
        
        :param feedbackDevice: Remote Feedback Device to select.
        
        :param pidIdx: 0 for Primary closed-loop. 1 for auxiliary closed-loop.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                      config success and report an error if it times out.
                      If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configSupplyCurrentLimit(self, currLimitConfigs, timeoutMs=50):  # real signature unknown; restored from __doc__
        """
        configSupplyCurrentLimit(self: ctre._ctre.TalonSRX, currLimitConfigs: ctre._ctre.SupplyCurrentLimitConfiguration, timeoutMs: int = 50) -> ctre._ctre.ErrorCode
        
        Configures the supply (input) current limit.
        
        :param currLimitConfigs: Current limit configuration
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                        config success and report an error if it times out.
                        If zero, no blocking or checking is performed.
        
        :returns: Error Code generated by function. 0 indicates no error.
        """
        pass

    def configurePID(self, pid, pidIdx=0, timeoutMs=50):  # real signature unknown; restored from __doc__
        """
        configurePID(self: ctre._ctre.TalonSRX, pid: ctre._ctre.TalonSRXPIDSetConfiguration, pidIdx: int = 0, timeoutMs: int = 50) -> ctre._ctre.ErrorCode
        
        Sets all PID persistant settings.
        
        :param pid: Object with all of the PID set persistant settings
        
        :param pidIdx: 0 for Primary closed-loop. 1 for auxiliary closed-loop.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        """
        pass

    def enableCurrentLimit(self, enable):  # real signature unknown; restored from __doc__
        """
        enableCurrentLimit(self: ctre._ctre.TalonSRX, enable: bool) -> None
        
        Enable or disable Current Limit.
        
        Supply current limiting is also available via ConfigSupplyCurrentLimit(),
        which is a common routine with Talon FX.
        
        :param enable: Enable state of current limit.
              @see configPeakCurrentLimit()
              @see configPeakCurrentDuration()
              @see configContinuousCurrentLimit()
        """
        pass

    def getAllConfigs(self, allConfigs, timeoutMs=50):  # real signature unknown; restored from __doc__
        """
        getAllConfigs(self: ctre._ctre.TalonSRX, allConfigs: ctre._ctre.TalonSRXConfiguration, timeoutMs: int = 50) -> None
        
        Gets all persistant settings.
        
        :param allConfigs: Object with all of the persistant settings
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                  config success and report an error if it times out.
                  If zero, no blocking or checking is performed.
        """
        pass

    def getPIDConfigs(self, pid, pidIdx=0, timeoutMs=50):  # real signature unknown; restored from __doc__
        """
        getPIDConfigs(self: ctre._ctre.TalonSRX, pid: ctre._ctre.TalonSRXPIDSetConfiguration, pidIdx: int = 0, timeoutMs: int = 50) -> None
        
        Gets all PID set persistant settings.
        
        :param pid: Object with all of the PID set persistant settings
        
        :param pidIdx: 0 for Primary closed-loop. 1 for auxiliary closed-loop.
        
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                 config success and report an error if it times out.
                 If zero, no blocking or checking is performed.
        """
        pass

    def getSensorCollection(self):  # real signature unknown; restored from __doc__
        """
        getSensorCollection(self: ctre._ctre.TalonSRX) -> ctre._ctre.SensorCollection
        
        
        
        :returns: object that can get/set individual RAW sensor values.
        """
        pass

    def set(self, *args, **kwargs):  # real signature unknown; restored from __doc__
        """
        set(*args, **kwargs)
        Overloaded function.
        
        1. set(self: ctre._ctre.TalonSRX, mode: ctre._ctre.TalonSRXControlMode, value: float) -> None
        
        Sets the appropriate output on the talon, depending on the mode.
        
        :param mode: The output mode to apply.
             In PercentOutput, the output is between -1.0 and 1.0, with 0.0 as stopped.
             In Current mode, output value is in amperes.
             In Velocity mode, output value is in position change / 100ms.
             In Position mode, output value is in encoder ticks or an analog value,
             depending on the sensor.
             In Follower mode, the output value is the integer device ID of the talon to
             duplicate.
        
        :param value: The setpoint value, as described above.
        
        
             Standard Driving Example:
             _talonLeft.set(ControlMode.PercentOutput, leftJoy);
             _talonRght.set(ControlMode.PercentOutput, rghtJoy);
        
        2. set(self: ctre._ctre.TalonSRX, mode: ctre._ctre.TalonSRXControlMode, demand0: float, demand1Type: ctre._ctre.DemandType, demand1: float) -> None
        
        
        
        :param mode: Sets the appropriate output on the talon, depending on the mode.
        
        :param demand0: The output value to apply.
                   such as advanced feed forward and/or auxiliary close-looping in firmware.
                   In PercentOutput, the output is between -1.0 and 1.0, with 0.0 as stopped.
                   In Current mode, output value is in amperes.
                   In Velocity mode, output value is in position change / 100ms.
                   In Position mode, output value is in encoder ticks or an analog value,
                   depending on the sensor. See
                   In Follower mode, the output value is the integer device ID of the talon to
                   duplicate.
        
        :param demand1Type: The demand type for demand1.
                   Neutral: Ignore demand1 and apply no change to the demand0 output.
                   AuxPID: Use demand1 to set the target for the auxiliary PID 1.  Auxiliary
                   PID is always executed as standard Position PID control.
                   ArbitraryFeedForward: Use demand1 as an arbitrary additive value to the
                   demand0 output.  In PercentOutput the demand0 output is the motor output,
                   and in closed-loop modes the demand0 output is the output of PID0.
        
        :param demand1: Supplmental output value.
                   AuxPID: Target position in Sensor Units
                   ArbitraryFeedForward: Percent Output between -1.0 and 1.0
        
        
                   Arcade Drive Example:
                   _talonLeft.set(ControlMode.PercentOutput, joyForward, DemandType.ArbitraryFeedForward, +joyTurn);
                   _talonRght.set(ControlMode.PercentOutput, joyForward, DemandType.ArbitraryFeedForward, -joyTurn);
        
                   Drive Straight Example:
                   Note: Selected Sensor Configuration is necessary for both PID0 and PID1.
                   _talonLeft.follow(_talonRght, FollwerType.AuxOutput1);
                   _talonRght.set(ControlMode.PercentOutput, joyForward, DemandType.AuxPID, desiredRobotHeading);
        
                   Drive Straight to a Distance Example:
                   Note: Other configurations (sensor selection, PID gains, etc.) need to be set.
                   _talonLeft.follow(_talonRght, FollwerType.AuxOutput1);
                   _talonRght.set(ControlMode.MotionMagic, targetDistance, DemandType.AuxPID, desiredRobotHeading);
        
        3. set(self: ctre._ctre.TalonSRX, mode: ctre._ctre.ControlMode, value: float) -> None
        
        4. set(self: ctre._ctre.TalonSRX, mode: ctre._ctre.ControlMode, demand0: float, demand1Type: ctre._ctre.DemandType, demand1: float) -> None
        """
        pass

    def __init__(self, deviceNumber):  # real signature unknown; restored from __doc__
        """
        __init__(self: ctre._ctre.TalonSRX, deviceNumber: int) -> None
        
        Constructor for a Talon
        
        :param deviceNumber: CAN Device ID of TalonSRX
        """
        pass
