
// �f���\��

class SosuInput {
	public static void main (String[] args) {
	
	System.out.println ("1�Ԗڂ̑f���� 1");
	int a = 2;
	
		for ( int n = 2 ; n <= 9000 ; n++) {
			for (int m = 2 ; m < n ; m++) {
				int p;
				p = n % m;
					
					if ( p == 0) {
						m = n -1;
					} else if (m < n -1) {
					} else {
					 	System.out.println (a +"�Ԗڂ̑f���� " + n);
					 	a++ ;
					}
				}
			}
		}
	}