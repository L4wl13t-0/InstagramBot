const puppeteer = require('puppeteer'); //Salimcan Satıcı
const fs = require('fs');
const USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36';

const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');
var Jimp = require('jimp');
var datos = [];

// Connection URL
//const url = 'mongodb://192.168.16.3:27017';
const url ='mongodb://localhost:27017';

// Database Name
const dbName = 'botsinstaPydb';
 
//mongodb: //localhost:27017/gmdproducto
//mongodb + srv: //darwin:Gmd123456@cluster0-wcnbe.mongodb.net/productosgmd1

// aqui 


const get_users = function(db, callback) {

    // Get the documents collection
    const usuarioBD = db.collection('users');
    // Find some documents

    // usuarioBD.find({}).toArray(function(err, usuarios) {
    usuarioBD.find({}).toArray(function(err, usuarios) {
        assert.equal(err, null);

        callback(usuarios);
    });
}


// Use connect method to connect to the server
MongoClient.connect(url, function(err, client) {
    assert.equal(null, err);
    console.log("Connected correctly to server");

    const db = client.db(dbName);


    get_users(db, async function(usuarios) {

        // se va ejecutar aqui tanto usuarios como existea


        for (const unUsuario in usuarios) {

            let nombreUsuario = await usuarios[unUsuario]['username'];
            let passwoUsuario = await usuarios[unUsuario]['password'];

            datos.push({
                'insta_username': nombreUsuario,
                'insta_password': passwoUsuario,

            });

            // console.log(datos);

        }

        client.close();
        // console.log("despues que cierra************",
        //datos);

        for (const unUsuario in datos) {

            let nombreUsuario = datos[unUsuario].insta_username;
            let claveUsuario = datos[unUsuario].insta_password;
            // console.log(nombreUsuario);

            (async() => {


                //Escribí el programa que vi en uno de ellos en el extranjero usando Nodejs + Puppeteer Chrome.
                //Uno de los primeros en el mercado.

                const browser = await puppeteer.launch({
                    headless: false,
                    defaultViewport: {
                        width: 1024,
                        height: 768,

                    },
                });
                const page = await browser.newPage();
                console.log(`Abrir navegador para el Usuario: ${nombreUsuario} `);
                await page.setUserAgent(USER_AGENT);
                // console.log("Usuario definido");
                await page.goto('https://www.instagram.com/accounts/edit/');
                // console.log("Reenvío de edición de Instagram proporcionado");
                await page.waitForSelector('input[name="username"]');
                //console.log("Estoy esperando que se cargue el campo de texto para que se cargue");
                //'odettatrevisan28' 
                //clave 'wjOV6o2X400o'
                await page.type('input[name="username"]', nombreUsuario); //Escriba su nombre de usuario en la parte que dice "SU NOMBRE DE USUARIO" SU NOMBRE DE USUARIO, es decir, sin eliminar las uñas
                // console.log("Kullanıcı adı textbox'ına kullanıcı adınız yazılıyor");
                await page.type('input[name="password"]', claveUsuario); //   Del mismo modo, no deje espacios en su parte de CONTRASEÑA.
                // console.log("Su contraseña está escrita en su cuadro de texto de contraseña.No hay absolutamente nada como enviar datos en el programa, de lo contrario, examine los códigos.Tu eres responsable.");

                await page.click('button[type="submit"]');
                // console.log("Hice clic en el botón de inicio de sesión.");
                blockingWait(4);
                await page.close(); //Manejar el error de navegación es un poco problemático y se ha realizado una pequeña transferencia de variable de página para que el módulo que utilizamos no falle.
                const sekme2 = await browser.newPage();
                await sekme2.setUserAgent(USER_AGENT);
                await sekme2.goto('https://www.instagram.com/accounts/edit/');
                const pageTitle = await sekme2.title();
                console.log(pageTitle)
                var inputElement = await sekme2.$('#react-root > section > main > div > article > div > div.LqNQc > div > div > form > input[type="file"]');
                X = Math.floor(Math.random() * 10)
                var photoNum = X; //Comienza desde la foto llamada 1.jpg 

                var fotogradedi = 24; //Por favor escriba la cantidad de fotos que tiene.

                for (let tekrar = 0; tekrar < 1; tekrar++) {
                    for (let index = 0; index < 1; index++) {
                        blockingWait(5);
                        inputElement.uploadFile('./resimler/' + photoNum + '.jpg');

                        console.log("Se cargará la Imagen con el siguiente número - > " + photoNum);
                        photoNum++;
                        if (photoNum == 20000000000) {
                            console.log("se repite");
                            photoNum = 1;
                        }
                    }
                }
            })();


        }

    });

});


// funcion de esperar 

function blockingWait(seconds) {
    //simple bloqueo de espera
    var waitTill = new Date(new Date().getTime() + seconds * 1000);
    while (waitTill > new Date()) {}
}