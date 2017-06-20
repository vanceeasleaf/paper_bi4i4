from aces import Aces
#the origin BP structure is optimized and we use it directly
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="Bi4I4_computed",
			method="greenkubo",
			nodes=1,
			procs=1,
			queue="q1.4",
			runTime=10000000
			,runner="shengbte"
		)
		app=dict(useMini=False,shengcut=-4,kpoints=[8,8,8],engine='vasp',supercell=[3,1,1],th=True,mekpoints=[4,4,4],ekpoints=[4,4,4])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
