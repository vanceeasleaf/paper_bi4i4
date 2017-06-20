from aces import Aces
#the origin BP structure is optimized and we use it directly
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="Bi4I4_computed",
			method="greenkubo",
			nodes=4,
			procs=12,
			queue="q1.1",
			runTime=10000000
			,runner="epw"
		)
		app=dict(nkf=[30,30,30],nqf=[30,30,30],ekpoints=[4,4,4],engine='vasp',useMini=False,kpoints=[4,3,2])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
