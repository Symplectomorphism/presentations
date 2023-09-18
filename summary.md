__Title__: Data-Driven Passivity Based Control of Robotic Locomotion and Manipulation

__Abstract__:
The recent boom and success of machine learning methods has encouraged efforts
in synthesizing controllers that leverage neural networks as function
approximators. However, when such controllers are synthesized it is important to
take precautions against their potential vulnerabilities against disturbances
arising from model uncertainties or measurement noise. In this work we address
the automatic robust data-driven controller synthesis problem for robotic
manipulation and locomotion. We demonstrate the efficacy of our theoretical
results in simulation and real-world experiments on a rimless-wheel and a
cart-pole system that contains walls. Our approach performs repeated
interactions with a nominal dynamical model to infer a contact-aware
passivity-based controller, whose storage function is given by a fully-connected
neural network. Contacts, impacts and Coulomb friction are modeled through the
linear complementarity problem (LCP), and solved via Lemke’s algorithm, which
allows us to take pertinent gradients for the data-driven technique.
Additionally, we improve the robustness properties of the controller under model
uncertainties, such as the rimless wheel traversing on uneven terrain, via
Bayesian learning. 

__Bio__:
Aykut Satici holds a BSc and MSc of Mechatronics Engineering from Sabanci
University in Turkey, an MSc of Mathematics, and Ph.D. in Electrical Engineering
from the University of Texas at Dallas under Prof. Mark W. Spong. He worked as a
postdoctoral associate at University of Naples, Federico II and at Massachusetts
Institute of Technology. Dr. Satici is currently an assistant professor of
Mechanical and Biomedical Engineering at Boise State University. He has actively
contributed to the control, estimation, and robotics research communities for
more than 15 years. His research output includes the optimal design of robotic
manipulators, optimal control of uncrewed aerial vehicles, multi-agent robot
control and estimation, differential geometric methods in nonlinear control,
passivity-based control, and control synthesis with machine learning methods. 
