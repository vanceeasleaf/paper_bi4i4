from aces import Aces
#the origin BP structure is optimized and we use it directly
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="Bi4I4",
			method="greenkubo",
			nodes=16,
			procs=4,
			queue="q3.4",
			runTime=10000000
			,runner="boltztrap_vasp"
		)
		app=dict(engine='vasp',useMini=False,ekpoints=[5,5,4])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
