using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CumleAnalizi
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string[] kelimeler = richTextBox1.Text.Split(new[] { " " }, StringSplitOptions.None);
            string uzunkelime = "";
            int karaktersayisi = 0;
            foreach (String kelime in kelimeler)
            {
                ListViewItem liste = new ListViewItem();
               
                liste.Text = kelime;
                liste.SubItems.Add(kelime.Length.ToString());
                listView1.Items.Add(liste);
            
                

                if (kelime.Length > karaktersayisi)
                {
                    uzunkelime = kelime;
                    karaktersayisi = kelime.Length;
                }
            }
            textBox1.Text = uzunkelime;

        }
    }
}
