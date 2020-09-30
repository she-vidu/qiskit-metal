# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019-2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

#pylint: disable-msg=unnecessary-pass
#pylint: disable-msg=broad-except
#pylint: disable-msg=unused-variable

"""
Qiskit Metal unit tests analyses functionality.

Test a planar deisgn and launching the GUI.

Created on  2020
@author: Zlatko K. Minev, Jeremy D. Drysdale
"""

import unittest
import inspect

from qiskit_metal import designs
from qiskit_metal import MetalGUI
from qiskit_metal._gui.widgets.bases.dict_tree_base import BranchNode
from qiskit_metal._gui.widgets.bases.dict_tree_base import LeafNode

from qiskit_metal.components.passives.capacitor_three_fingers import Capacitor3Fingers
from qiskit_metal.components.passives.launch_v1 import LaunchV1
from qiskit_metal.components.passives.launch_v2 import LaunchV2
from qiskit_metal.components.passives.three_finger_cap_v1 import ThreeFingerCapV1
from qiskit_metal.components.qubits.transmon_concentric import TransmonConcentric
from qiskit_metal.components.qubits.transmon_cross import TransmonCross
from qiskit_metal.components.qubits.transmon_pocket import TransmonPocket
from qiskit_metal.components.qubits.transmon_pocket_cl import TransmonPocketCL

class TestGUIBasic(unittest.TestCase):
    """
    Unit test class
    """

    def setUp(self):
        """
        Setup unit test
        """
        pass

    def tearDown(self):
        """
        Tie any loose ends
        """
        pass

    def test_gui_01_launch(self):
        """
        Test the functionality of launching the GUI.
        01 added to the test name so it is the first GUI to launch

        Single function used for all GUI stuff with general catch-all so:
          a. multiple GUI windows causing problems in CI
          b. we can catch any errors

        Raises:
            Exception: Any exceptions raised during attempted launch
        """
        try:
            design = designs.DesignPlanar()

            q_1 = TransmonCross(design, 'Q1', options=dict(pos_x='-1.5mm', pos_y='+0.0mm'))
            q_2 = TransmonPocket(design, 'Q2', options=dict(pos_x='+1.5mm', pos_y='+0.0mm'))
            q_3 = TransmonPocketCL(design, 'Q3', options=dict(pos_x='+0.0mm', pos_y='+1.0mm'))
            q_4 = TransmonConcentric(design, 'Q4', options=dict(pos_x='+3.0mm', pos_y='+3.0mm'))

            cap_1 = Capacitor3Fingers(design, 'C1', options=dict(pos_x='-2.0mm', pos_y='-2.0mm'))
            cap_2 = LaunchV1(design, 'C2', options=dict(pos_x='-2.0mm', pos_y='0.0mm'))
            cap_3 = LaunchV2(design, 'C3', options=dict(pos_x='-2.0mm', pos_y='-0.5mm'))
            cap_4 = ThreeFingerCapV1(design, 'C4', options=dict(pos_x='-2.0mm', pos_y='-1.0mm'))

            gui = MetalGUI(design)
            gui.autoscale()
            gui.refresh()
            gui.rebuild()
        except Exception:
            my_name = inspect.stack()[0][3]
            self.fail(my_name + " threw an exception.  GUI failure")

    def test_instantiate_branch_node(self):
        """
        Test instantiation of BranchNode in dict_tree_base.py
        """
        try:
            BranchNode('my_name')
        except Exception:
            message = "BranchNode instantiation failed"
            self.fail(message)

    def test_instantiate_leaf_node(self):
        """
        Test instantiation of LeafNode in dict_tree_base.py
        """
        try:
            LeafNode('my_label')
        except Exception:
            message = "LeafNode instantiation failed"
            self.fail(message)

if __name__ == '__main__':
    unittest.main(verbosity=2)
