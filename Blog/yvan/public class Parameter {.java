public class Parameter {
    public static void main(String[] args) {
        if (args.length == 0) {
            return;
        }
        int a = 42;
        fun(a, args);
        System.out.println(a + "," + args[0]);
        String[] array = new String[] { "Swapped!" };
        swap(array, args);
        System.out.println(args[0]);
    }

    public static void fun(int a, String[] array) {
        a = array.length;
        array[0] = "Hello!";
    }

    public static void swap(String[] a, String[] b) {
        String[] tmp = a;
        a = b;
        b = tmp;
    }
}
