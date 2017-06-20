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
			,runner="shengbte"
		)
		app=dict(vdw=True,encut=520,th=True,useMini=True,shengcut=-4,kpoints=[8,8,8],engine='vasp',supercell=[3,2,2],mekpoints=[9,6,4],ekpoints=[3,3,2])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
