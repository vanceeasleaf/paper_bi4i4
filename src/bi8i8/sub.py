from aces import Aces
#the origin BP structure is optimized and we use it directly
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="Bi8I8",
			method="greenkubo",
			nodes=12,
			procs=4,
			queue="q3.4",
			runTime=10000000
			,runner="shengbte"
		)
		app=dict(laty=2,th=True,shengcut=-4,kpoints=[2,20,3],engine='vasp',supercell=[1,2,1],mekpoints=[4,4,4],ekpoints=[2,2,2])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
