/*
 * @author ArabianCoconut
 * @version 1.0
 * @since 1.0
 * Time taken for class Value_1000 = for 2 Arrays respectively is 6 and 15 milliseconds
 * Time taken for class Value_10000 = for 2 Arrays respectively is 43 and 42 milliseconds
 * Time taken for class Value_100000 = for 2 Arrays respectively is 2021 and 2009 milliseconds
 */

import java.util.Arrays;
public class benchmarking {
    //Global Variables for array
    public static int[] array;
    public static int[] array2;
    public static void selectionSort(int[] array) {
        // selection sort the array
        for (int i = 0; i < array.length - 1; i++) {
            int index = i;
            for (int j = i + 1; j < array.length; j++)
                if (array[j] < array[index])
                    index = j;
            int smallerNumber = array[index];
            array[index] = array[i];
            array[i] = smallerNumber;
        }
    }

    // Sorting and Selection Sort for 1000 elements
    static class value_1000{
        public static void main(String[] args) {
            // make 2 arrays of 1000 elements
            array = new int[1000];
            array2 = new int[1000];
            // append them with random numbers max 1000 elements
            for (int i = 0; i < 1000; i++) {
                array[i] = (int) (Math.random() * 1000);
                // clone array to array2
                array2=array.clone();
            }
            // sort the arrays and time it
            long Array_1_Time = System.currentTimeMillis();
            Arrays.sort(array);
            // Selection sort the array2
            long Array_2_Time = System.currentTimeMillis();
            selectionSort(array2);
            // Print the time taken for each array
            System.out.println("Time taken for Array 1 value 1,000 using sort() : " + (System.currentTimeMillis() - Array_1_Time ) +"ms");
            System.out.println("Time taken for Array 2 value 1,000 using selectionSort(): " + (System.currentTimeMillis() - Array_2_Time) +"ms");
        }

    }
    // Sorting and Selection sort for 10,000 elements
    static class value_10000 {
        public static void main(String[] args) {
            // Make two Array with int  with random numbers maximum 10000
            int Max_Value_10000 = 10000;
            array = new int[(int) (Math.random() * Max_Value_10000)];
            array2 = new int[(int) (Math.random() * Max_Value_10000)];
            // append array with random numbers total length of array is 10000
            for (int i = 0; i < array.length; i++) {
                array[i] = (int) (Math.random() * 10000);
                // clone array to array2
                array2=array.clone();
            }

            // sort the array1 and time it
            long startTimeArray1 = System.currentTimeMillis();
            Arrays.sort(array);
            // selection sort the array and time it
            long startTimeArray2 = System.currentTimeMillis();
            selectionSort(array2);
            // Array print time
            System.out.println("Time taken for Array 1 value 10,000 using sort(): " + (System.currentTimeMillis() - startTimeArray1) + "ms");
            // Array2 print time
            System.out.println("Time taken for Array 2 value 10,000 using SelectionSort() : " + (System.currentTimeMillis() - startTimeArray2) + "ms");
        }
    }
    // Sorting and Selection sort for 100,000 elements
    // WARNING DO NOT RUN THIS IF YOUR PC IS NOT FAST ENOUGH
    static class value_100000 {
        public static void main(String[] args) {
            // Make two Array with int  with random numbers maximum 100000
            int Max_Value_100000 = 100000;
            array = new int[(int) (Math.random() * Max_Value_100000)];
            array2 = new int[(int) (Math.random() * Max_Value_100000)];
            // append array with random numbers total length of array is 100000
            for (int i = 0; i < array.length; i++) {
                array[i] = (int) (Math.random() * 100000);
            }
            // clone array to array2
            array2=array.clone();
            // sort the array2  and time it
            long startTimeArray = System.currentTimeMillis();
            Arrays.sort(array);
            // selection sort the array and time it
            long startTimeArray2 = System.currentTimeMillis();
            selectionSort(array2);
            // Array print time
            System.out.println("Time taken for Array 1 for 100,000 using Sort(): " + (System.currentTimeMillis() - startTimeArray) + "ms");
            // Array2 print time
            System.out.println("Time taken for Array 2 for 100,000 using SelectionSort(): " + (System.currentTimeMillis() - startTimeArray2) + "ms");
        }
    }

    public static void main(String[] args) {
        // Run the classes
        value_1000.main(args);
        value_10000.main(args);
        value_100000.main(args); // WARNING DO NOT RUN THIS IF YOUR PC IS SLOW IF YOU CAN RUN IT JUST UNCOMMENT THIS LINE
    }
}
