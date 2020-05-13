#!/usr/bin/env python
# coding: utf-8

# In[108]:


from qiskit import *
get_ipython().run_line_magic('matplotlib', 'inline')
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from qiskit.providers.ibmq import least_busy


# In[110]:


def NOT(input):
    circuit = QuantumCircuit(1,1)
    
    if input == '1':
        circuit.x(0)
    
    circuit.x(0)
    
    circuit.measure(0, 0)
    provider = IBMQ.get_provider('ibm-q')
    b = provider.get_backend('ibmq_london')
    
    job = execute(circuit, backend=b)
    job_monitor(job)
    result = job.result()
    return plot_histogram(result.get_counts(circuit))
NOT('1')


# In[111]:


# one bit or
def XOR(input1, input2):
    circuit = QuantumCircuit(2,1)
    if input1 == '1':
        circuit.x(0)
    if input2 == '1':
        circuit.x(1)
    
    circuit.cx(0, 1)
    circuit.measure(1,0)
    
    # 1 0 -> 1
    # 1 1 -> 0
    
    
    provider = IBMQ.get_provider('ibm-q')
    b = provider.get_backend('ibmq_london')
    
    job = execute(circuit, backend=b)
    job_monitor(job)
    result = job.result()
    return plot_histogram(result.get_counts(circuit))
XOR('1', '0')


# In[112]:


def AND(input1, input2):
    circuit = QuantumCircuit(3,1)
    if input1 == '1':
        circuit.x(0)
    if input2 == '1':
        circuit.x(1)
    circuit.ccx(0, 1, 2)
    circuit.measure(2,0)
    
    provider = IBMQ.get_provider('ibm-q')
    b = provider.get_backend('ibmq_london')
    
    job = execute(circuit, backend=b)
    job_monitor(job)
    result = job.result()
    return plot_histogram(result.get_counts(circuit))
AND('1','1')


# In[102]:


def NAND(input1, input2):
    circuit = QuantumCircuit(3, 1)
    if input1 == '1':
        circuit.x(0)
    if input2 == '1':
        circuit.x(1)
    circuit.ccx(0, 1, 2)
    circuit.x(2)
    circuit.measure(2, 0)
    

    provider = IBMQ.get_provider('ibm-q')
    b = provider.get_backend('ibmq_london')
    
    job = execute(circuit, backend=b)
    job_monitor(job)
    result = job.result()
    return plot_histogram(result.get_counts(circuit))
NAND('1','1')


# In[113]:


def OR(input1, input2):
    circuit = QuantumCircuit(3, 1)
    if input1 == '0':
        circuit.x(0)
    if input2 == '0':
        circuit.x(1)
        
    
    circuit.ccx(0, 1, 2)
    circuit.x(2)
    circuit.measure(2,0)
    
    provider = IBMQ.get_provider('ibm-q')
    b = provider.get_backend('ibmq_london')
    
    job = execute(circuit, backend=b)
    job_monitor(job)
    result = job.result()
    return plot_histogram(result.get_counts(circuit))
OR('1','0')


# In[114]:


def half_adder(input1, input2):
    circuit = QuantumCircuit(5, 5)
    if input1 == '1':
        circuit.x(0)
    if input2 == '1':
        circuit.x(1)
        
    circuit.ccx(0, 1, 3) # carry
    circuit.cx(0, 1) # sum
    circuit.barrier()
    circuit.measure(1, 0)
    circuit.measure(3, 1)
    
    provider = IBMQ.get_provider('ibm-q')
    b = provider.get_backend('ibmq_london')
    
    job = execute(circuit, backend=b)
    job_monitor(job)
    result = job.result()
    return plot_histogram(result.get_counts(circuit))
half_adder('1','0')


# In[ ]:




