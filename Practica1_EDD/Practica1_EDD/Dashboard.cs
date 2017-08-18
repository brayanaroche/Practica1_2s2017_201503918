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
            //metodo_POST();
           // metodo_GET();
        }

        //variable para el cliete en c#
        //private static readonly HttpClient cliente = new HttpClient();
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
            // Create a request using a URL that can receive a post. 
            WebRequest request = WebRequest.Create("http://0.0.0.0:5000/Dashboard");
            // Set the Method property of the request to POST.
            request.Method = "POST";
            // Create POST data and convert it to a byte array.
            string postData = "This is a test that posts this string to a Web server.";
            byte[] byteArray = Encoding.UTF8.GetBytes(postData);
            // Set the ContentType property of the WebRequest.
            request.ContentType = "application/x-www-form-urlencoded";
            // Set the ContentLength property of the WebRequest.
            request.ContentLength = byteArray.Length;
            // Get the request stream.
            Stream dataStream = request.GetRequestStream();
            // Write the data to the request stream.
            dataStream.Write(byteArray, 0, byteArray.Length);
            // Close the Stream object.
            dataStream.Close();
            // Get the response.
            WebResponse response = request.GetResponse();
            // Display the status.
            Console.WriteLine(((HttpWebResponse)response).StatusDescription);
            // Get the stream containing content returned by the server.
            dataStream = response.GetResponseStream();
            // Open the stream using a StreamReader for easy access.
            StreamReader reader = new StreamReader(dataStream);
            // Read the content.
            string responseFromServer = reader.ReadToEnd();
            // Display the content.
            Console.WriteLine(responseFromServer);
            // Clean up the streams.
            reader.Close();
            dataStream.Close();
            response.Close();

        }
    }
}
