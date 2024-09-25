namespace ParabolicInterpolation
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.plotView1 = new OxyPlot.WindowsForms.PlotView();
            this.buttonDraw = new System.Windows.Forms.Button();
            this.textBoxP1X = new System.Windows.Forms.TextBox();
            this.textBoxP2X = new System.Windows.Forms.TextBox();
            this.textBoxP3X = new System.Windows.Forms.TextBox();
            this.textBoxP4X = new System.Windows.Forms.TextBox();
            this.textBoxP1Y = new System.Windows.Forms.TextBox();
            this.textBoxP2Y = new System.Windows.Forms.TextBox();
            this.textBoxP3Y = new System.Windows.Forms.TextBox();
            this.textBoxP4Y = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.timer1 = new System.Windows.Forms.Timer(this.components);
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // plotView1
            // 
            this.plotView1.Location = new System.Drawing.Point(12, 12);
            this.plotView1.Name = "plotView1";
            this.plotView1.PanCursor = System.Windows.Forms.Cursors.Hand;
            this.plotView1.Size = new System.Drawing.Size(734, 301);
            this.plotView1.TabIndex = 0;
            this.plotView1.Text = "plotView1";
            this.plotView1.ZoomHorizontalCursor = System.Windows.Forms.Cursors.SizeWE;
            this.plotView1.ZoomRectangleCursor = System.Windows.Forms.Cursors.SizeNWSE;
            this.plotView1.ZoomVerticalCursor = System.Windows.Forms.Cursors.SizeNS;
            this.plotView1.Click += new System.EventHandler(this.plotView1_Click);
            // 
            // buttonDraw
            // 
            this.buttonDraw.Location = new System.Drawing.Point(684, 333);
            this.buttonDraw.Name = "buttonDraw";
            this.buttonDraw.Size = new System.Drawing.Size(62, 57);
            this.buttonDraw.TabIndex = 1;
            this.buttonDraw.Text = "Draw";
            this.buttonDraw.UseVisualStyleBackColor = true;
            this.buttonDraw.Click += new System.EventHandler(this.buttonDraw_Click);
            // 
            // textBoxP1X
            // 
            this.textBoxP1X.Location = new System.Drawing.Point(0, 370);
            this.textBoxP1X.Name = "textBoxP1X";
            this.textBoxP1X.Size = new System.Drawing.Size(29, 20);
            this.textBoxP1X.TabIndex = 2;
            // 
            // textBoxP2X
            // 
            this.textBoxP2X.Location = new System.Drawing.Point(101, 370);
            this.textBoxP2X.Name = "textBoxP2X";
            this.textBoxP2X.Size = new System.Drawing.Size(29, 20);
            this.textBoxP2X.TabIndex = 3;
            // 
            // textBoxP3X
            // 
            this.textBoxP3X.Location = new System.Drawing.Point(207, 370);
            this.textBoxP3X.Name = "textBoxP3X";
            this.textBoxP3X.Size = new System.Drawing.Size(29, 20);
            this.textBoxP3X.TabIndex = 4;
            // 
            // textBoxP4X
            // 
            this.textBoxP4X.Location = new System.Drawing.Point(309, 370);
            this.textBoxP4X.Name = "textBoxP4X";
            this.textBoxP4X.Size = new System.Drawing.Size(29, 20);
            this.textBoxP4X.TabIndex = 5;
            // 
            // textBoxP1Y
            // 
            this.textBoxP1Y.Location = new System.Drawing.Point(35, 370);
            this.textBoxP1Y.Name = "textBoxP1Y";
            this.textBoxP1Y.Size = new System.Drawing.Size(29, 20);
            this.textBoxP1Y.TabIndex = 6;
            // 
            // textBoxP2Y
            // 
            this.textBoxP2Y.Location = new System.Drawing.Point(136, 370);
            this.textBoxP2Y.Name = "textBoxP2Y";
            this.textBoxP2Y.Size = new System.Drawing.Size(29, 20);
            this.textBoxP2Y.TabIndex = 7;
            // 
            // textBoxP3Y
            // 
            this.textBoxP3Y.Location = new System.Drawing.Point(242, 370);
            this.textBoxP3Y.Name = "textBoxP3Y";
            this.textBoxP3Y.Size = new System.Drawing.Size(29, 20);
            this.textBoxP3Y.TabIndex = 8;
            // 
            // textBoxP4Y
            // 
            this.textBoxP4Y.Location = new System.Drawing.Point(344, 370);
            this.textBoxP4Y.Name = "textBoxP4Y";
            this.textBoxP4Y.Size = new System.Drawing.Size(29, 20);
            this.textBoxP4Y.TabIndex = 9;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(70, 373);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(20, 13);
            this.label1.TabIndex = 10;
            this.label1.Text = "P1";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(171, 373);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(20, 13);
            this.label2.TabIndex = 11;
            this.label2.Text = "P2";
            this.label2.Click += new System.EventHandler(this.label2_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(277, 373);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(20, 13);
            this.label3.TabIndex = 12;
            this.label3.Text = "P3";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(379, 373);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(20, 13);
            this.label4.TabIndex = 13;
            this.label4.Text = "P4";
            // 
            // timer1
            // 
            this.timer1.Tick += new System.EventHandler(this.timer1_Tick);
            // 
            // textBox1
            // 
            this.textBox1.Enabled = false;
            this.textBox1.Location = new System.Drawing.Point(428, 333);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(203, 57);
            this.textBox1.TabIndex = 15;
            this.textBox1.Text = "Задавати точки потрібно зліва на право по Х і будь якими значеннями по У але щоб " +
    "параболи перетинались";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.textBoxP4Y);
            this.Controls.Add(this.textBoxP3Y);
            this.Controls.Add(this.textBoxP2Y);
            this.Controls.Add(this.textBoxP1Y);
            this.Controls.Add(this.textBoxP4X);
            this.Controls.Add(this.textBoxP3X);
            this.Controls.Add(this.textBoxP2X);
            this.Controls.Add(this.textBoxP1X);
            this.Controls.Add(this.buttonDraw);
            this.Controls.Add(this.plotView1);
            this.Name = "Form1";
            this.Text = "ParabolicDraw";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private OxyPlot.WindowsForms.PlotView plotView1;
        private System.Windows.Forms.Button buttonDraw;
        private System.Windows.Forms.TextBox textBoxP1X;
        private System.Windows.Forms.TextBox textBoxP2X;
        private System.Windows.Forms.TextBox textBoxP3X;
        private System.Windows.Forms.TextBox textBoxP4X;
        private System.Windows.Forms.TextBox textBoxP1Y;
        private System.Windows.Forms.TextBox textBoxP2Y;
        private System.Windows.Forms.TextBox textBoxP3Y;
        private System.Windows.Forms.TextBox textBoxP4Y;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Timer timer1;
        private System.Windows.Forms.TextBox textBox1;
    }
}

