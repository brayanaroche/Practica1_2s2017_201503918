using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Practica1_EDD
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Form1 form = new Form1();
            //form.Hide();
            Dashboard das = new Dashboard();
            das.Show();
            this.Hide();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            AdminMen adminmen = new AdminMen();
            adminmen.Show();
            this.Hide();
        }
    }
}
