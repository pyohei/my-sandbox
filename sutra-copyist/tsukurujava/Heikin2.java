public class Heikin2 {
	public static void main (String[] args) {
		int [] ten;
		double heikin;
		
		ten = new int[3];
		//��x����`�����
		ten [0] = 63;
		ten [1] = 53;
		ten [2] = 46;
		heikin = (ten [0] + ten [1] + ten [2] ) / 3;
		
		System.out.println ("���ς̌v�Z���ʂ�" + ten[1] + "�ł͂Ȃ��[" + heikin + "�ł����[�I");
	}
}