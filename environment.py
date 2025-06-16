class GridEnvironment:
	def __init__(self, rows=5, cols=5, start=(0,0), goal=(4,4), walls=None):
		self.rows=rows
		self.cols=cols
		self.start = start
		self.goal = goal
		self.walls = walls if walls else []
		self.reset()

	def reset(self):
		self.agent_position = self.start
		return self.agent_position

	def is_valid(self,position):
		r,c = position
		if(0<= r<self.rows) and (0<=c < self.cols) and (position not in self.walls):
			return True
		return False

	def step(self,action):
		r,c = self.agent_position
		moves = {
		"up": (r-1,c),
		"down": (r+1,c),
		"left":	(r, c-1),
		"right":(r,c+1)
		}

		next_position = moves.get(action, self.agent_position)

		if self.is_valid(next_position):
			self.agent_position = next_position
		else:
			next_position =self.agent_position

		reward =10 if next_position==self.goal else -1
		done = next_position == self.goal
	
		return next_position, reward, done
