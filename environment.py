# -*- coding: utf-8 -*-
import blabla
import threading
import math
import actions
import reward
import buzz_python
import itertools


class Environment(buzz_python.session_subscriber):
    def __init__(self, _buoys_list, _step, _vessel_id, _rudder_id, _thr_id, _scn, _goal, _plot):
        super(Environment, self).__init__()
        self.buoys = _buoys_list
        self.goal = _goal
        self.steps_between_actions = _step
        # self.vessel_id = '102'
        self.vessel_id = _vessel_id
        self.rudder_id = _rudder_id
        self.thruster_id = _thr_id
        # self.mongo_addr = 'mongodb://10.1.1.92:27017'
        # self.dbname = 'test'
        self.simulation_id = 'sim'
        # self.scenario = 'Santos_Container_L349B45'
        self.scenario = _scn
        self.control_id = '555'
        self.chat_address = '127.0.0.1'
        self.simulation = []
        self.dyna_ctrl_id = '407'
        self.allow_advance_ev = threading.Event()
        self.dyna_ready_ev = threading.Event()
        self.own = []
        self.vessel = []
        self.rudder = []
        self.thruster = []
        self.max_angle = 0
        self.max_rot = 0
        self.reward_mapper = reward.RewardMapper(_plot)
        self.init_state = list()
        self._final_flag = False
        self.initial_states_sequence = list()

    def get_initial_states(self):
        positions_dict = self.reward_mapper.generate_inner_positions()
        init_angles = (-90, -110, -130)
        states_list = list()
        for position in positions_dict:
            for angle in init_angles:
                state = (position[0], position[1], angle, positions_dict[position]/5000,0,0)
                states_list.append(state)
        return states_list

    def is_final(self):
        ret = 0
        if self.reward_mapper.reached_goal():
            ret = 1
        elif self.reward_mapper.collided():
            ret = -1
        return ret

    def on_state_changed(self, state):
        if state == buzz_python.STANDBY:
            print("Dyna ready")
            self.dyna_ready_ev.set()

    def on_time_advanced(self, time):
        step = self.simulation.get_current_time_step()

    def on_time_advance_requested(self, process):
        if process.get_id() == self.dyna_ctrl_id:
            self.allow_advance_ev.set()

    def set_up(self):
        # ds = buzz_python.create_bson_data_source(self.mongo_addr, self.dbname)
        ds = buzz_python.create_bson_data_source('suape-local.json')
        ser = buzz_python.create_bson_serializer(ds)
        self.simulation = buzz_python.create_simco_simulation(self.simulation_id, self.control_id, ser)
        self.simulation.connect(self.chat_address)
        self.init(self.simulation)
        scn = ser.deserialize_scenario(self.scenario)
        self.simulation.add(scn)
        factory = self.simulation.get_element_factory()
        r_c = factory.build_runtime_component(self.dyna_ctrl_id)
        self.simulation.add(r_c)
        self.own = self.simulation.get_runtime_component(self.control_id)

        self.simulation.build()
        self.simulation.set_current_time_increment(0.1)
        self.reward_mapper.set_boundary_points(self.buoys)
        self.reward_mapper.set_goal(self.goal)

        self.start()
        self.vessel = self.simulation.get_vessel(self.vessel_id)
        # self.initial_states_sequence = self.get_initial_states()
        # self.init_state = self.get_state() #TODO remove this temporary line
        self.initial_states_sequence = itertools.cycle(self.get_initial_states())

        self.init_state = next(self.initial_states_sequence)
        # self.reset_state(self.init_state[0], self.init_state[1], self.init_state[2],
        #                      self.init_state[3], self.init_state[4], self.init_state[5])
        # self.reward_mapper.update_ship(-200, -200, 10,, 0, 0
        self.simulation.advance_time()
        self.advance()
        self.advance()
        self.get_propulsion()

    def start(self):
        self.dyna_ready_ev.wait()
        self.simulation.start()
        self.dyna_ready_ev.clear()

    def get_propulsion(self):
        thr_tag = buzz_python.thruster_tag()
        self.simulation.is_publisher(thr_tag, thr_tag.SMH_DEMANDED_ROTATION)

        rdr_tag = buzz_python.rudder_tag()
        self.simulation.is_publisher(rdr_tag, rdr_tag.SMH_DEMANDED_ANGLE)

        thr_ev_taken_tag = buzz_python.thruster_control_taken_event_tag()
        self.simulation.is_publisher(thr_ev_taken_tag, True)

        rdr_ev_taken_tag = buzz_python.rudder_control_taken_event_tag()
        self.simulation.is_publisher(rdr_ev_taken_tag, True)

        self.thruster = self.vessel.get_thruster(self.thruster_id)
        ctrl_ev = buzz_python.create_thruster_control_taken_event(self.thruster)
        ctrl_ev.set_controlled_fields(thr_tag.SMH_DEMANDED_ROTATION)
        ctrl_ev.set_controller(self.own)
        self.simulation.publish_event(ctrl_ev)

        self.rudder = self.vessel.get_rudder(self.rudder_id)
        ctrl_ev_r = buzz_python.create_rudder_control_taken_event(self.rudder)
        ctrl_ev_r.set_controlled_fields(rdr_tag.SMH_DEMANDED_ANGLE)
        ctrl_ev_r.set_controller(self.own)
        self.simulation.publish_event(ctrl_ev_r)
        self.simulation.update(self.thruster)
        self.max_rot = self.thruster.get_maximum_rotation()
        self.simulation.update(self.rudder)
        self.max_angle = self.rudder.get_maximum_angle()

    def get_state(self):
        self.simulation.sync(self.vessel)
        lin_pos_vec = self.vessel.get_linear_position()
        ang_pos_vec = self.vessel.get_angular_position()
        lin_vel_vec = self.vessel.get_linear_velocity()
        ang_vel_vec = self.vessel.get_angular_velocity()
        x = lin_pos_vec[0]
        y = lin_pos_vec[1]
        theta = ang_pos_vec[2]
        xp = lin_vel_vec[0]
        yp = lin_vel_vec[1]
        thetap = ang_vel_vec[2]
        return x, y, theta, xp, yp, thetap

    def advance(self):
        self.allow_advance_ev.wait()
        self.simulation.advance_time()
        self.allow_advance_ev.clear()

    def step(self, action):
        """**Implement Here***
            The state transition. The agent executed the action in the parameter
        """
        cycle = 0
        for cycle in range(self.steps_between_actions):
            self.advance()
        print(action)
        rot_level, angle_level = actions.map_from_action(action)
        self.thruster.set_demanded_rotation(rot_level*self.max_rot)
        self.simulation.update(self.thruster)
        self.rudder.set_demanded_angle(angle_level*self.max_angle)
        self.simulation.update(self.rudder)
        statePrime = self.get_state() #Get next State

        self.reward_mapper.update_ship(statePrime[0], statePrime[1], statePrime[2],statePrime[3], statePrime[4],
                                       statePrime[5])
        rw = self.reward_mapper.get_reward()
        print(self.reward_mapper.collided())
        if self.reward_mapper.collided():
            print("Collided!!!")
            self.init_state = next(self.initial_states_sequence)
            self.reset_state(self.init_state[0], self.init_state[1], self.init_state[2],
                             self.init_state[3], self.init_state[4], self.init_state[5])
            statePrime = self.get_state()  # Get next State
        return statePrime, action, rw

    def reset_state(self, x, y, theta, vel_x, vel_y, vel_theta):
        self.vessel.set_linear_position([x, y, 0.00])
        self.vessel.set_linear_velocity([vel_x, vel_y, 0.00])
        self.vessel.set_angular_position([0.00, 0.00, theta])
        self.vessel.set_angular_velocity([0.00, 0.00, vel_theta])
        self.simulation.sync(self.vessel)

    def __del__(self):
        if self.simulation:
            self.simulation.stop()
            self.simulation.disconnect()


if __name__ == "__main__":
    test = Environment()
    test.set_up()
    for i in range(100):
        ret = test.step(i)
        print(ret)