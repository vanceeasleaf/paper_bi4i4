from aces.graph import fig,pl
with fig("a.png"):
	pl.xlabel("ZT")
	pl.ylabel("Thermoelectric Efficiency")
	import numpy as np
	t2=900.0;t1=300.0
	t=(t1+t2)/2.0
	zt=np.linspace(0,4.0,100)
	x=np.sqrt(1.0+zt)
	eta=(t2-t1)/t2*(x-1)/(t1/t2+x)
	pl.plot(zt,eta,linewidth=2)
	zt=np.arange(5.0)
	x=np.sqrt(1.0+zt)
	eta=(t2-t1)/t2*(x-1)/(t1/t2+x)
	pl.plot(zt,eta,'or')
