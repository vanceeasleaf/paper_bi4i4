from aces import Aces
#the origin BP structure is optimized and we use it directly
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="Bi4I4",
			method="greenkubo",
			nodes=1,
			procs=12,
			queue="q1.1",
			runTime=10000000
			,runner="shengbte"
		)
		app=dict(shengcut=-4,kpoints=[8,8,8],engine='vasp',supercell=[2,2,2],mekpoints=[4,4,4],ekpoints=[2,2,2])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
