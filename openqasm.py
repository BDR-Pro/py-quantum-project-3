from qiskit import qasm3 
from qiskit import *

qc=QuantumCircuit(4,4) 

qc.h(0)
qc.h(1)
qc.h(2)
qc.x(3)
qc.h(3)

qc.barrier()

qc.cx(0,1)
qc.cx(1,2)
qc.cx(2,3)

qc.barrier()

qc.h(0)
qc.h(1)
qc.h(2)
qc.h(3)


qc.measure(0,0)
qc.measure(1,1)
qc.measure(2, 2)

qc.draw(output='mpl')

qasm_string = qasm3.dumps(qc, experimental=qasm3.ExperimentalFeatures.SWITCH_CASE_V1)
print(qasm_string)