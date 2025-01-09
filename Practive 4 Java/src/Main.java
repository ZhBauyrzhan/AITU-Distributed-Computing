import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.IntStream;

public class Main {

    public static BufferedImage parallelProgram(BufferedImage image) {
        int height = image.getHeight();
        int width = image.getWidth();
        BufferedImage result = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        IntStream.range(0, height)
                .parallel()
                .forEach(y -> {
                    for (int x = 0; x < width; x++) {
                        Color color = new Color(image.getRGB(x, y));
                        int red = Math.min(255, color.getRed() + 50);
                        result.setRGB(x, y, new Color(red, red, red).getRGB());
                    }
                });
        return result;
    }

    public static BufferedImage multiThreadProgram(BufferedImage image, int numThreads) {
        ExecutorService executor = Executors.newFixedThreadPool(numThreads);
        int height = image.getHeight();
        int blockHeight = height / numThreads;
        int width = image.getWidth();
        BufferedImage result = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
        for (int i = 0; i < numThreads; i++) {
            final int startY = i * blockHeight;
            final int endY = (i == numThreads - 1) ? height : startY + blockHeight;
            executor.submit(() -> {
                for (int y = startY; y < endY; y++) {
                    for (int x = 0; x < width; x++) {
                        Color color = new Color(image.getRGB(x, y));
                        int red = Math.min(255, color.getRed() + 50);
                        result.setRGB(x, y, new Color(red, red, red).getRGB());
                    }
                }
            });
        }
        return result;
    }

    public static void showImages(BufferedImage image, BufferedImage image2) {
        JFrame frame = new JFrame();
        frame.getContentPane().setLayout(new FlowLayout());
        frame.getContentPane().add(new JLabel(new ImageIcon(image)));
        frame.getContentPane().add(new JLabel(new ImageIcon(image2)));
        frame.pack();
        frame.setVisible(true);
    }

    public static void main(String[] args) throws IOException {
        File img1 = new File("src/kobe1.jpeg");
        BufferedImage in = ImageIO.read(img1);
        long startTime = System.currentTimeMillis();
        BufferedImage result1 = parallelProgram(in);
        long endTime = System.currentTimeMillis();
        System.out.println("That took " + (endTime - startTime) + " milliseconds");
        File outputfile = new File("src/image.jpeg");
        ImageIO.write(result1, "jpeg", outputfile);
        showImages(in, result1);

        File img2 = new File("src/2.jpeg");
        BufferedImage in2 = ImageIO.read(img2);

        startTime = System.currentTimeMillis();
        BufferedImage result2 = multiThreadProgram(in2, 2);
        endTime = System.currentTimeMillis();
        System.out.println("That took " + (endTime - startTime) + " milliseconds");
        File outputfile2 = new File("src/image2.jpeg");
        ImageIO.write(result2, "jpeg", outputfile2);
        showImages(in2, result2);


        startTime = System.currentTimeMillis();
        BufferedImage result3 = multiThreadProgram(in2, 4);
        endTime = System.currentTimeMillis();
        System.out.println("That took " + (endTime - startTime) + " milliseconds");
        File outputfile3 = new File("src/image3.jpeg");
        ImageIO.write(result3, "jpeg", outputfile3);
        showImages(in2, result3);
    }
}
