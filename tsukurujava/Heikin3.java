import java.io.*;

public class Heikin3 {
	public static void main (String[] args) throws IOException {
	BufferedReader br = new BufferedReader (new InputStreamReader (System.in));
	
	System.out.println("���w�̓_����ǉ����Ă�������");
	String str1 =br.readLine();
	System.out.println("�Љ�̓_����ǉ����Ă�������");
	String str2 =br.readLine();
	
	int a = Integer.parseInt(str1);
	int b = Integer.parseInt(str2);
	int [] ten;
	double sum1;
	double sum2;
	double heikin;
	
	ten = new int [2];
	ten [0] = 49;
	ten [1] = 89;
	sum1 = 0;
	sum2 = 0;
	
	for (int i = 0; i < 2; i++) {
		sum1 = sum1 + ten [i];
	}
	
	sum2 = sum1 + a +b;
	heikin = sum2 / 4;
	
	System.out.println ( "�p��" + ten[0] + "�_�A����" + ten[1] + "�_");
	System.out.println ( "������������w�̓_����" + a + "�_");
	System.out.println ( "����������Љ�̓_����" + b + "�_");
	System.out.println ( "����Ď�v4�Ȗڂ̕��ς�" + heikin + "�_");
	}
}