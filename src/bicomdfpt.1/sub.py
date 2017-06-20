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
			,runner="phonopy_dfpt"
		)
		app=dict(ispin=True,useMini=False,kpoints=[8,8,8],engine='vasp',latx=3,supercell=[1,1,1],ekpoints=[3,3,3])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
