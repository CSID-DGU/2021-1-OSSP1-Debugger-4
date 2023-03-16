const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const morgan = require("morgan");
const multer = require("multer");
var http = require('http');
const app = express();
const util = require('util');
require('util.promisify').shim();
const fs = require('fs');
const readFileAsync = util.promisify(fs.readFile);

const upload = multer({
  storage: multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, '../server/uploads/');
    },
    filename: function (req, file, cb) {
      cb(null, file.originalname);
    }
  }),
});


app.use(cors());
app.use(morgan("combined"));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/image",function(req,res)
{
    res.sendFile('/home/plass-sukhyun/2021-1-OSSP1-Debugger-4/preprocess/result.png');
});

app.post("/", upload.array("file[]"), function(req, res)  {
  req.setTimeout(60000000000);
  console.log(req.files);

var {PythonShell} = require('python-shell');
var options = {

  mode: 'text',
  pythonPath: '',
  pythonOptions: ['-u'],
  scriptPath: '',

};

//python child process 생성 
let pyshell = new PythonShell('../2021-1-OSSP1-Debugger-4/facesynthesis.py', options)
pyshell.end((err, code, signal) => {
	if(err) throw err;
  	res.end();
});

});


const port = process.env.PORT || 3001;
app.listen(port, () =>{
	console.log("Upload Server running on 3001...");
});




