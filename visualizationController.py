class VisualizationController:
    def __init__(self, tanks_area):
        self._tanks_area = tanks_area

    def set_tank_level(self, tank, level):
        tank.setPoziom(level)
        self.sync_pipe_flow()

    def toogle_pump(self, running):
        if self._tanks_area.pump.isRunning():
            self._tanks_area.pump.stop()
        else:
            self._tanks_area.pump.start()
        self.sync_pipe_flow()

    def set_valve_state(self, state):
        self._tanks_area.valve.changeState(state)
        self.sync_pipe_flow()

    def set_heater_state(self, state):
        self._tanks_area.heater.changeState(state)

    def set_temperature(self, value):
        self._tanks_area.set_temperature(value)

    def sync_pipe_flow(self):
        area = self._tanks_area
        area.pipe4.ustaw_przeplyw(area.pump.isRunning())

        if area.tank1.getPoziom() > 0:
            area.pipe2.ustaw_przeplyw(True)
            area.pipe3.ustaw_przeplyw(area.valve.getState())
        else:
            area.pipe2.ustaw_przeplyw(False)
            area.pipe3.ustaw_przeplyw(False)


    def set_temperature(self, value):
        self._tanks_area.labels.set_temperature(value)