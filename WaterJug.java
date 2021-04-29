import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class WaterJug {
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////	
	public class State {
		int x;
		int y;
		State p;
		
		public State(int x, int y, WaterJug.State p) {
			this.x = x;
			this.y = y;
			this.p = p;
		}

		@Override
		public String toString() {
			StringBuilder builder = new StringBuilder();
	        if (p != null) {
	            builder.append(p);
	        }
	        builder.append("(").append(x);
	        builder.append("   ").append(y).append(")").append("\n");
	        return builder.toString();
		}

		@Override
		public boolean equals(Object obj) {
	        if (this == obj) {
	            return true;
	        }
	        if (obj == null) {
	            return false;
	        }
	        if (getClass() != obj.getClass()) {
	            return false;
	        }
	        State other = (State) obj;
	        if (this.x != other.x) {
	            return false;
	        }
	        if (this.y != other.y) {
	            return false;
	        }
	        return true;
		}		
		

		
	}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	public class StateManager{
		Queue<State> queue = new LinkedList<>();
		List<State> checkedState = new LinkedList<>();
		int a, b, c;
		
		
		
		public boolean checkExistState(int x, int y) {
			State nextState = new State(x, y, null);
			if(!checkedState.contains(nextState)) {
				checkedState.add(nextState);
				return false;
			}
			else return true;
		}
		
//		public boolean check(State state , int x, int y) {
//			if(state.p == null) return false;
//			if(state.x == x && state.y == y) return true;
//			return check(state.p, x, y);
//		}
		
		public void checkAndAddState(State curState) {
			//Fill Jug if it is empty
			if(curState.x == 0) {
				if(!checkExistState(a, curState.y)) queue.add(new State(a, curState.y, curState));
			}
			if(curState.y == 0) {
				if(!checkExistState(curState.x, b)) queue.add(new State(curState.x, b, curState));
			}
			
			//Empty Jug
			if(curState.x > 0) {
				if(!checkExistState(0, curState.y)) queue.add(new State(0, curState.y, curState));
			}
			if(curState.y > 0) {
				if(!checkExistState(curState.x, 0)) queue.add(new State(curState.x, 0, curState));
			}
			
			//Pour Jug 1 to Jug 2
			if(curState.x > 0 && curState.x + curState.y >= b) {
				if(!checkExistState(curState.x + curState.y - b, b)) queue.add(new State(curState.x + curState.y - b, b, curState));
			}
			if(curState.x > 0 && curState.x + curState.y < b) {
				if(!checkExistState(0, curState.x + curState.y)) queue.add(new State(0, curState.x + curState.y, curState));
			}
			//Pour Jug 2 to Jug 1
			if(curState.y > 0 && curState.x + curState.y >= a) {
				if(!checkExistState(a, curState.x + curState.y - a)) queue.add(new State(a, curState.x + curState.y - a, curState));
			}
			if(curState.y > 0 && curState.x + curState.y < a) {
				if(!checkExistState(curState.x + curState.y, 0)) queue.add(new State(curState.x + curState.y, 0, curState));
			}
		}
		
		public boolean finalState(int x, int y) {
			if(x == c || y == c || x + y == c) return true;
			else return false;
		}
		
		public State popFront() {
			State state = null;
			if(!queue.isEmpty()) state = queue.poll();
			return state;
		}
		
		public void genInitialStage() {
			initialState = new State (0, 0, null);
			queue.add(initialState);
			checkedState.add(initialState);
		}
		
		public void loopQueue() {
			State finalState = null;
			while(!queue.isEmpty()) {
				State curState = popFront();
				if(finalState(curState.x, curState.y)) {
					finalState = curState;
					break;
				}
				checkAndAddState(curState);
			}
			if(finalState != null) {
				System.out.println(finalState.toString());
			}else System.out.println("No Answer!");
		}
	}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////	
	public class WaterJugSlover{
		WaterJug wj = new WaterJug();
		StateManager sm = wj.new StateManager();
		public void slove(int a, int b, int c) {
			sm.a = a;
			sm.b = b;
			sm.c = c;
			sm.genInitialStage();
			sm.loopQueue();
		}
	}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////	
	
	
	State initialState;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a, b, c;
		WaterJug wj = new WaterJug();
		WaterJugSlover wjs = wj.new WaterJugSlover();
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter Jug 1 capacity: ");
		a = sc.nextInt();
		System.out.print("Enter Jug 1 capacity: ");
		b = sc.nextInt();
		System.out.print("Enter Target volume: ");
		c = sc.nextInt();
		wjs.slove(a, b, c);
		sc.close();
		
	}

}
