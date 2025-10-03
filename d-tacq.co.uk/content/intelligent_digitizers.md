# Intelligent Digitizer Concept
<tooltip title="D-TACQ High Performance Simultaneous Data Acquisition">D-TACQ</tooltip> digitizers feature an array of discrete <tooltip title="Analog to Digital Convertor">ADC</tooltip> devices, one convertor per channel.

This differs from most digitizer cards, which will use a single <tooltip title="Analog to Digital Convertor">ADC</tooltip> device with a multiplexer to route each channel in sequence onto the <tooltip title="Analog to Digital Convertor">ADC</tooltip> in turn. The <tooltip title="Analog to Digital Convertor">ADC</tooltip>-per-channel approach became cost-effective with the advent of fast and accurate integrated <tooltip title="Successive Approximation Register (class of ADC with Excellent DC accuracy)">SAR</tooltip> convertor devices, and offers the following advantages over the multiplexer approach:

*  Simultaneous Sampling - all convertors sample the data on the same clock edge
*  Much Higher throughput.
*  Inherently better crosstalk
*  Suitable for Low Latency control applications

<tooltip title="D-TACQ High Performance Simultaneous Data Acquisition">D-TACQ</tooltip> digitizers also feature an on-board microprocessor and a deep DRAM memory buffer. The microprocessor is a low cost, low power device, but is able to give great flexibility in data and memory management.

The first product in the range, ACQ32PCI was released in 1999 and, configured as "DT100" systems - Industrial PC, x86 host running Linux and making use of the deep capture memory, ACQ32PCI found immediate application in transient capture diagnostics. ACQ32PCI deployed applications range from streaming data from a single card in a spinning centrifuge to advanced low latency control applications with more than 128 channels.

Finally, the digitizers feature a state-of-the art <tooltip title="Field Programmable Gate Array">FPGA</tooltip> device, controlling all aspects of clocking and data flow. The latest <tooltip title="Field Programmable Gate Array">FPGA</tooltip> devices also offer considerable possibilities for real time signal processing.