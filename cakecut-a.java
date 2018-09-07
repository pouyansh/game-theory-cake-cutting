import java.util.Arrays;
import java.util.Comparator;
import java.util.Random;
import java.util.Scanner;

public class Ans {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        double[] startTimes = new double[n], finishTimes = new double[n];
        setaii[] tempStarts = new setaii[n], tempFinishes = new setaii[n];
        for (int i = 0; i < n; i++) {
            startTimes[i] = scanner.nextDouble();
            finishTimes[i] = scanner.nextDouble();
            tempStarts[i] = new setaii(startTimes[i], i);
            tempFinishes[i] = new setaii(finishTimes[i], i);
        }
        Arrays.sort(tempStarts, new Comparator<setaii>() {
            @Override
            public int compare(setaii o1, setaii o2) {
                return Double.compare(o1.getFirst(), o2.getFirst());
            }
        });
        double[] ptrs = new double[n + 1];
        ptrs[n] = 100;
        for (int i = 0; i < n; i++) {
            ptrs[i] = tempStarts[i].getFirst();
        }
        Arrays.sort(tempFinishes, new Comparator<setaii>() {
            @Override
            public int compare(setaii o1, setaii o2) {
                return Double.compare(o1.getFirst(), o2.getFirst());
            }
        });
        int ptrptrs = 1;
        int sum = 0;
        while (ptrptrs < n) {
            sum++;
            if (ptrptrs == 0) {
                ptrptrs++;
                continue;
            }
            //System.out.println(ptrptrs + " " + ptrs[ptrptrs-1] + " " +  ptrs[ptrptrs] + " " + ptrs[ptrptrs+1]);
            if (ptrs[ptrptrs] - comp(ptrs[ptrptrs - 1], tempStarts[ptrptrs - 1].getFirst()) <= compar(ptrs[ptrptrs + 1], tempFinishes[ptrptrs - 1].getFirst()) - ptrs[ptrptrs]) {
                if ((ptrs[ptrptrs] - ((comp(ptrs[ptrptrs - 1], tempStarts[ptrptrs].getFirst()) + compar(ptrs[ptrptrs + 1], tempFinishes[ptrptrs].getFirst()))/2.0)) >= 1e-5 ||
                        (ptrs[ptrptrs] - ((comp(ptrs[ptrptrs - 1], tempStarts[ptrptrs].getFirst()) + compar(ptrs[ptrptrs + 1], tempFinishes[ptrptrs].getFirst()))/2.0)) <= -1e-7) {
                    ptrs[ptrptrs] = (comp(ptrs[ptrptrs - 1], tempStarts[ptrptrs].getFirst()) + compar(ptrs[ptrptrs + 1], tempFinishes[ptrptrs].getFirst())) / 2;
                    ptrs[ptrptrs] += (comp(ptrs[ptrptrs - 1], tempStarts[ptrptrs - 1].getFirst()) + compar(ptrs[ptrptrs + 1], tempFinishes[ptrptrs - 1].getFirst())) / 2;
                    ptrs[ptrptrs] /= 2;
                    ptrptrs--;
                    continue;
                }
            }
            if (ptrs[ptrptrs] - comp(ptrs[ptrptrs - 1], tempStarts[ptrptrs].getFirst()) >= compar(ptrs[ptrptrs + 1], tempFinishes[ptrptrs].getFirst()) - ptrs[ptrptrs]) {
                if ((ptrs[ptrptrs]-((comp(ptrs[ptrptrs - 1], tempStarts[ptrptrs - 1].getFirst()) + compar(ptrs[ptrptrs + 1], tempFinishes[ptrptrs - 1].getFirst()))/2.0))>=1e-5 ||
                        (ptrs[ptrptrs]-((comp(ptrs[ptrptrs - 1], tempStarts[ptrptrs - 1].getFirst()) + compar(ptrs[ptrptrs + 1], tempFinishes[ptrptrs - 1].getFirst()))/2.0))<=-1e-7) {
                    ptrs[ptrptrs] = (comp(ptrs[ptrptrs - 1], tempStarts[ptrptrs].getFirst()) + compar(ptrs[ptrptrs + 1], tempFinishes[ptrptrs].getFirst())) / 2;
                    ptrs[ptrptrs] += (comp(ptrs[ptrptrs - 1], tempStarts[ptrptrs - 1].getFirst()) + compar(ptrs[ptrptrs + 1], tempFinishes[ptrptrs - 1].getFirst())) / 2;
                    ptrs[ptrptrs] /= 2;
                    ptrptrs--;
                    continue;
                }
            }
            ptrptrs++;
        }
        //System.out.println(sum);
        for (int i = 1; i < n; i++) {
            System.out.printf("%.7f ", ptrs[i]);
        }
        System.out.println();
        for (int i = 0; i < n; i++) {
            System.out.print((tempStarts[i].getSecond() + 1) + " ");
        }
        System.out.println();
    }

    private static double comp(double a, double b) {
        if (a > b) return a;
        return b;
    }

    private static double compar(double a, double b) {
        if (a > b) return b;
        return a;
    }
}

class setaii implements Comparable<setaii> {
    private double time;
    private int adam;

    setaii(double first, int second) {
        this.time = first;
        this.adam = second;
    }

    double getFirst() {
        return time;
    }

    int getSecond() {
        return adam;
    }

    @Override
    public int compareTo(setaii o) {
        if (o.getFirst() > this.time) {
            return 1;
        }
        return 0;
    }
}
