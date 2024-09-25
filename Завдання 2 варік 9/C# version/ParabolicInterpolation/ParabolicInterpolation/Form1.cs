using OxyPlot;
using OxyPlot.Series;
using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace ParabolicInterpolation
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }

        public double[] MultiplyVectorOnMatrix(double[] Vect, double[,] Matr)
        {
            double[] resultVect = new double[4];

            for (int j = 0; j < Vect.Length; ++j)
            {
                resultVect[j] = 0;
                for (int k = 0; k < Vect.Length; ++k)
                {
                    resultVect[j] += Vect[k] * Matr[k, j];
                }
            }
            return resultVect;
        }
        public Point MultiplyVectorOnVector(double[] vect, Point[] points)
        {
            Point pointRs = new Point(0, 0);


            for (int k = 0; k < 4; ++k)
            {
                pointRs.x += vect[k] * points[k].x;
            }
            for (int k = 0; k < 4; ++k)
            {
                pointRs.y += vect[k] * points[k].y;
            }

            return Decrease(pointRs);
        }

        public Point Decrease(Point point)
        {
            return new Point(point.x * 0.5, point.y * 0.5);
        }

        public Point GetCPoint(double f, Point p1, Point p2, Point p3, Point p4)
        {
            double[] vect = new double[4];
            vect[0] = f * f * f;
            vect[1] = f * f;
            vect[2] = f;
            vect[3] = 1;
            double[,] matrix ={
            {-1, 3, -3, 1},
            {2, -5, 4, -1},
            {-1, 0, 1, 0},
            {0, 2, 0, 0}
            };
            double[] Res = MultiplyVectorOnMatrix(vect, matrix);
            Point[] points = { p1, p2, p3, p4 };
            Point res = MultiplyVectorOnVector(Res, points);
            return res;
        }
        public void DrawCurves(Point p1, Point p2, Point p3, Point p4, PlotModel model)
        {
            Point temp = GetCPoint(0, p1, p2, p3, p4);
            Point next = temp;
            LineSeries line = new LineSeries();

            for (double t = 0; t <= 1; t += 0.01)
            {
                temp = next;
                next = GetCPoint(t, p1, p2, p3, p4);
                line.Points.Add(new DataPoint(temp.x, temp.y));
            }
            model.Series.Add(line);
        }
        public void DrawFigure(double[] xList, List<double> yList, PlotModel model)
        {
            List<DataPoint> points = new List<DataPoint>();
            LineSeries line = new LineSeries();
            for (int i = 0; i < xList.Length; i++)
            {
                line.Points.Add(new DataPoint(xList[i], yList[i]));
            }
            model.Series.Add(line);

        }
        private void Form1_Load(object sender, EventArgs e)
        {
            this.plotView1.Show();

        }
        public double findInterpolatedY(double[] xArray, double[] yArray, double x)
        {
            double result = 0;
            int index1 = 1;
            int index2 = 2;
            for (int i = 0; i < 3; i++)
            {
                result += yArray[i] * ((x - xArray[index1]) * (x - xArray[index2])
                               / ((xArray[i] - xArray[index1]) * (xArray[i] - xArray[index2])));
                index1 += 1;
                index2 += 1;

                if (index1 % 3 == 0)
                {
                    index1 = 0;
                }
                if (index2 % 3 == 0)
                {
                    index2 = 0;
                }
            }
            return result;
        }

        private void buttonDraw_Click(object sender, EventArgs e)
        {
            Point[] points = new Point[4];

            points[0] = (new Point(-1, 0));
            points[1] = (new Point(0, 5));
            points[2] = (new Point(10, -5));
            points[3] = (new Point(20, 0));

            //points[0] = (new Point(double.Parse(this.textBoxP1X.Text), double.Parse(this.textBoxP1Y.Text)));
            //points[1] = (new Point(double.Parse(this.textBoxP2X.Text), double.Parse(this.textBoxP2Y.Text)));
            //points[2] = (new Point(double.Parse(this.textBoxP3X.Text), double.Parse(this.textBoxP3Y.Text)));
            //points[3] = (new Point(double.Parse(this.textBoxP4X.Text), double.Parse(this.textBoxP4Y.Text)));

            double[] xPoints1 = new double[3];
            xPoints1[0] = (points[0].x);
            xPoints1[1] = (points[1].x);
            xPoints1[2] = (points[2].x);

            double[] yPoints1 = new double[3];
            yPoints1[0] = (points[0].y);
            yPoints1[1] = (points[1].y);
            yPoints1[2] = (points[2].y);

            double[] xPoints2 = new double[3];
            xPoints2[0] = (points[1].x);
            xPoints2[1] = (points[2].x);
            xPoints2[2] = (points[3].x);

            double[] yPoints2 = new double[3];
            yPoints2[0] = (points[1].y);
            yPoints2[1] = (points[2].y);
            yPoints2[2] = (points[3].y);

            var n = points[2].x;// найюільше значення по х для параболи 1
            List<double> yInterpolated1 = new List<double>();
            List<double> yInterpolated2 = new List<double>();
            for (double i = points[0].x; i < n; i += 0.1)
            {
                yInterpolated1.Add(findInterpolatedY(xPoints1, yPoints1, i));
            }
            n = points[3].x;// найюільше значення по х для параболи 2
            for (double i = points[1].x; i < n; i += 0.1)
            {
                yInterpolated2.Add(findInterpolatedY(xPoints2, yPoints2, i));
            }
            double[] xForInterpolated1 = new double[yInterpolated1.Count];
            double[] xForInterpolated2 = new double[yInterpolated2.Count];
            double count = points[0].x;
            for (int i = 0; i < xForInterpolated1.Length; i++)
            {
                xForInterpolated1[i] = count;
                count += 0.1;
            }
            count = points[1].x;
            for (int i = 0; i < xForInterpolated2.Length; i++)
            {
                xForInterpolated2[i] = count;
                count += 0.1;
            }
            var myModel = new PlotModel { Title = "Plot" };

            DrawFigure(xForInterpolated1, yInterpolated1, myModel);

            DrawFigure(xForInterpolated2, yInterpolated2, myModel);

            DrawCurves(points[0], points[1], points[2], points[3], myModel);

            this.plotView1.Model = myModel;
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.plotView1.Refresh();
        }

        private void plotView1_Click(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }
    }
}
