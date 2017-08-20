using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net;
using System.Web;
using System.IO;
using RestSharp;

namespace Practica1_EDD
{
    public partial class Dashboard : Form
    {
        public Dashboard()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            metodo_POST();
           // metodo_GET();
        }
        private async void metodo_Get()
        {
            string baseurl = "http://127.0.0.1:5000/hola";
            HttpWebRequest conexion = (HttpWebRequest)HttpWebRequest.Create(baseurl);
            conexion.Method= "GET";
            Stream lectura = conexion.GetResponse().GetResponseStream();

            StreamReader reader = new StreamReader(lectura);

            string prueba = reader.ReadLine();
            MessageBox.Show(prueba);

            //var valores = new Dictionary<string, string>
            //{
            //    { "hola", "Hello World Brayan aroche"}
            //};

            //var contenedor = new FormUrlEncodedContent(valores);
            
            //var respuesta = await cliente.PostAsync("127.0.0.1:5000/", contenedor);

            //var respuestaCadena = await respuesta.Content.ReadAsStringAsync();
        }

        private async void metodo_POST() {
            try
            {

                //Abriendo archivo para obtener el path

                OpenFileDialog abrir_archivo = new OpenFileDialog();
                abrir_archivo.Title = "Seleccionar Archivo";

                if (abrir_archivo.ShowDialog() == System.Windows.Forms.DialogResult.OK)
                {
                    StreamReader leer = new StreamReader(abrir_archivo.FileName);
                    leer.Close();
                }

                string direccion = abrir_archivo.FileName;

                MessageBox.Show("la ruta es: " + direccion);
                var cliente = new RestClient("http://127.0.0.1:5000/ArchivoJson");

                var request = new RestRequest("/", Method.POST);

                request.AddParameter("ruta", direccion);

                IRestResponse respuesta = cliente.Execute(request);

                var contenido = respuesta.Content;
                webBrowser1.Navigate(respuesta.Content);
            }
            catch (Exception e) {
                Console.WriteLine("Se produjo un error: " + e);
            }
            //webBrowser1.DocumentText = respuesta.Content;
            //MessageBox.Show("el contenido de vuelta es: " + contenido);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form1 inicio = new Form1();
            inicio.Show();
            this.Hide();
        }
    }
}
