# FPGA Capability
<tooltip>DTACQ</tooltip> cards use an advanced Field Programmable Gate Array FPGA for data marshalling. The configuration image for the <tooltip>FPGA</tooltip> is held in local flash memory, allowing for easy in system upgrade. The devices used on the 2G series of cards have sufficient spare capacity to perform significant real time DSP on captured data in real time as it passes through the <tooltip>FPGA</tooltip>. <tooltip>DTACQ</tooltip> has implemented a range of standard DSP functions to ship with the data, including

*  Event detection
*  Digital Filter $DEFS[FIR] for use in oversampling applications, brick wall anti alias filter, processing gain, more effective bits <a href="oversampling_fir_filter.shtml">example</a>.
*  Timestamp functions
*  Thresholding and peak detect

In addition, custom processing may be implemented. Typically <tooltip>DTACQ</tooltip> will supply a skeleton application to end-user requirement, and the end-user may then choose to complete the design . Examples of custom processing implemented in FPGA include:

* <a href="digital-lock-in-amplifier.shtml">96 channel digital lock-in amplifier</a> :<br/><i>	synchronous detection brings enormous processing gain.</i>
* 96 channel digital down-converter DDC :<br/><i>	 8x data shifting a modulated signal from carrier to baseband.</i>
* Klystron [Microwave] coupler protection system. :<br/><i> very hard realtime math based protection system, 200+ channels on 16 cards.</i>