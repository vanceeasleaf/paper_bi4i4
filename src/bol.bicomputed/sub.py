from aces import Aces
#the origin BP structure is optimized and we use it directly
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="Bi4I4_computed",
			method="greenkubo",
			nodes=8,
			procs=12,
			queue="q1.4",
			runTime=10000000
			,runner="boltztrap_vasp"
		)
		app=dict(engine='vasp',useMini=False,ekpoints=[4,4,4])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
