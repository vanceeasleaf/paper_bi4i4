from aces import Aces
#the origin BP structure is optimized and we use it directly
class sub(Aces):
	def submit(self):
		opt=dict(
			units="metal",
			species="Bi4I4c",
			method="greenkubo",
			nodes=1,
			procs=12,
			queue="q1.4",
			runTime=10000000
			,runner="boltztrap_vasp"
		)
		app=dict(isym=False,soc=True,engine='vasp',useMini=False,ekpoints=[10,10,10])
		self.commit(opt,app);
if __name__=='__main__':
	sub().run()
